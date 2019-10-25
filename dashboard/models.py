from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _
from decimal import Decimal


class Earnings(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='earnings')

    earning_date = models.DateTimeField(_('Date'))
    hits = models.IntegerField(_('Hits'), default=0)
    leads = models.IntegerField(_('Leads'), default=0)
    money = models.DecimalField(_('Money'), max_digits=6, decimal_places=2)

    class Meta:
        ordering = ('-earning_date',)


class Payments(models.Model):
    TYPE_CHOICES = [
        ('regular', 'Regular'),
        ('commercial', 'Commercial'),
        ('progress', 'Progress'),
    ]
    STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
    ]

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payments')

    payment_date = models.DateTimeField(_('Date'))
    invoice_id = models.IntegerField(_('Invoice ID'))
    type = models.CharField(max_length=32, choices=TYPE_CHOICES, null=True, default=TYPE_CHOICES[0][0])
    amount = models.DecimalField(_('Amount'), max_digits=6, decimal_places=2)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, null=True, default=STATUS_CHOICES[0][0])

    class Meta:
        ordering = ('-payment_date',)


class SmartLinks(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='smartlinks')
    smart_link = models.CharField(_('Smart Link'), max_length=255)

    class Meta:
        ordering = ['-id']


class SupportManager(models.Model):
    AVATAR_CHOICES = [
        ('m-01', 'Male-01'),
        ('f-01', 'Female-01'),
        ('m-02', 'Male-02'),
        ('f-02', 'Female-02'),
        ('m-03', 'Male-03'),
        ('f-03', 'Female-03'),
        ('m-04', 'Male-04'),
        ('f-04', 'Female-04'),
        ('m-05', 'Male-05'),
        ('f-05', 'Female-05'),
        ('m-06', 'Male-06'),
        ('f-06', 'Female-06'),
        ('m-07', 'Male-07'),
        ('f-07', 'Female-07'),
        ('m-08', 'Male-08'),
        ('f-08', 'Female-08'),
        ('m-09', 'Male-09'),
        ('f-09', 'Female-09'),
        ('m-10', 'Male-10'),
        ('f-10', 'Female-10')
    ]
    name = models.CharField(_('full name'), max_length=255)
    avatar = models.CharField(_('avatar'), max_length=32, choices=AVATAR_CHOICES, null=True,
                              default=AVATAR_CHOICES[0][0])
    email = models.EmailField(_('email address'), max_length=255)
    phone_number = models.CharField(_('phone number'), max_length=60)
    skype = models.CharField(_('skype'), max_length=255, null=True, blank=True)
    website = models.CharField(_('website'), max_length=255, null=True, blank=True)

    class Meta:
        ordering = ['-id']


class Balance(models.Model):
    customer = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='balance')
    balance = models.DecimalField(_('Balance'), max_digits=6, default=Decimal('0.00'), decimal_places=2)

    class Meta:
        ordering = ['-id']
