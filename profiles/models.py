from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.mail import send_mail
from django.db import models
from django.db.models import Sum
from django.utils import timezone
from django.utils.translation import ugettext as _
from dashboard.models import Balance
from decimal import Decimal


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = UserManager.normalize_email(email)

        extra_fields.pop('username', None)  # Passed by social auth, not needed here

        user = self.model(email=email, is_staff=False, is_active=True, is_superuser=False, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        u = self.create_user(email, password, **extra_fields)
        u.is_staff = True
        u.is_active = True
        u.is_superuser = True
        u.save(using=self._db)
        return u

    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD + '__iexact': username})


class User(AbstractBaseUser):
    email = models.EmailField(_('email address'), unique=True)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.')
    )
    is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=_('Designates whether this user should be treated as active. '
                    'Unselect this instead of deleting accounts.')
    )

    is_superuser = models.BooleanField(
        _('Is superuser?'),
        default=False,
        help_text=_('Designates that this user has all permissions without explicitly assigning them.')
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['-id']

    def _get_name(self):
        profile = self.profile
        if profile:
            return {"first": profile.first_name,
                    "last": profile.last_name}
        else:
            return None

    def get_full_name(self):
        return u"{0} {1}".format(self.first_name, self.last_name).strip() or self.email

    def get_balance(self):
        if Balance.objects.filter(customer=self).count() == 0:
            Balance.objects.create(customer=self, balance=Decimal('0.00'))

        return Balance.objects.filter(customer=self).aggregate(Sum('balance'))['balance__sum']

    def get_short_name(self):
        return self.first_name or self.email.split('@')[0]

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.email

    @property
    def is_email_confirmed(self):
        return self.profile.is_email_confirmed


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    # Details
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)

    username = models.CharField(max_length=100, null=True, blank=True)

    phone_number = models.CharField(_('phone number'), max_length=60, blank=True)

    is_email_confirmed = models.BooleanField(default=False)

    class Meta:
        ordering = ('first_name', 'last_name')

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        if self.first_name and self.last_name:
            full_name = u'{} {}'.format(self.first_name, self.last_name)
            return full_name.strip()
        return self.user.email.split('@')[0]

    def get_short_name(self):
        return self.first_name

    @property
    def is_active(self):
        return self.is_email_confirmed

    def get_email(self):
        return self.user.email

