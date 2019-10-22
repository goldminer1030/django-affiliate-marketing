from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext as _


class Earnings(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='earnings')

    date = models.DateTimeField(_('Date'), default=timezone.now)
    hits = models.IntegerField(_('Hits'), default=0)
    leads = models.IntegerField(_('Leads'), default=0)
    money = models.DecimalField(_('Money'), max_digits=6, decimal_places=2)

    class Meta:
        ordering = ('-date',)


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

    date = models.DateTimeField(_('Date'), default=timezone.now)
    invoice_id = models.IntegerField(_('Invoice ID'))
    type = models.CharField(max_length=32, choices=TYPE_CHOICES, null=True, default=TYPE_CHOICES[0][0])
    amount = models.DecimalField(_('Amount'), max_digits=6, decimal_places=2)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, null=True, default=STATUS_CHOICES[0][0])

    class Meta:
        ordering = ('-date',)


class SmartLinks(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='smartlinks')
    smart_link = models.CharField(_('Smart Link'), max_length=255)
