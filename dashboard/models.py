from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _


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


class ContactInfo(models.Model):
    customer = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contact')

    address = models.CharField(_('address'), max_length=255, null=True, blank=True)
    email = models.EmailField(_('email address'), max_length=255, null=True, blank=True)
    phone_number = models.CharField(_('phone number'), max_length=60, null=True, blank=True)
    website = models.CharField(_('website'), max_length=255, null=True, blank=True)
    skype = models.CharField(_('skype'), max_length=255, null=True, blank=True)
    linkedin = models.CharField(_('linkedin'), max_length=255, null=True, blank=True)
    instagram = models.CharField(_('instagram'), max_length=255, null=True, blank=True)
    twitter = models.CharField(_('twitter'), max_length=255, null=True, blank=True)
    facebook = models.CharField(_('facebook'), max_length=255, null=True, blank=True)

    class Meta:
        ordering = ['-id']
