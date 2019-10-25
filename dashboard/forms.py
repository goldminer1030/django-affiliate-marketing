from django import forms
from django.forms import widgets
from django.utils.safestring import mark_safe
from decimal import Decimal
from bootstrap_modal_forms.forms import BSModalForm
from .models import SmartLinks, Earnings, Payments, SupportManager, Balance
from profiles.models import User

TYPE_CHOICES = [
    ('regular', 'Regular'),
    ('commercial', 'Commercial'),
    ('progress', 'Progress'),
]
STATUS_CHOICES = [
    ('paid', 'Paid'),
    ('unpaid', 'Unpaid'),
]


class SmartLinksForm(BSModalForm):
    customer = forms.ModelChoiceField(queryset=User.objects.all().order_by('email'), widget=forms.Select(),
                                      empty_label=None)

    smart_link = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control m-input m-input--square', 'placeholder': 'Smart Link'})
    )

    class Meta:
        model = SmartLinks
        fields = ('customer', 'smart_link')


class DateTimePickerWidget(widgets.TextInput):
    def render(self, name, value, attrs=None, renderer=None):
        return mark_safe(u'''<div class="input-group date" id="id_%s" data-target-input="nearest">%s<div class=
        "input-group-append" data-target="#id_%s" data-toggle="datetimepicker"><div class="input-group-text">
        <i class="far fa-calendar-alt"></i></div></div></div>''' %
                         (name, super(DateTimePickerWidget, self).render(name, value, attrs), name))


class EarningsForm(BSModalForm):
    customer = forms.ModelChoiceField(queryset=User.objects.all().order_by('email'), widget=forms.Select(),
                                      empty_label=None)

    earning_date = forms.DateTimeField(
        widget=DateTimePickerWidget(attrs={
            'class': 'form-control datetimepicker-input',
            'id': 'earning_date',
            'data-target': '#id_earning_date'
        })
    )

    hits = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'min': '0'
    }))

    leads = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'min': '0'
    }))

    money = forms.DecimalField(widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }), min_value=Decimal('0.00'))

    class Meta:
        model = Earnings
        fields = ('customer', 'earning_date', 'hits', 'leads', 'money')


class PaymentsForm(BSModalForm):
    customer = forms.ModelChoiceField(queryset=User.objects.all().order_by('email'), widget=forms.Select(),
                                      empty_label=None)

    payment_date = forms.DateTimeField(
        widget=DateTimePickerWidget(attrs={
            'class': 'form-control',
            'id': 'payment_date',
            'data-target': '#id_payment_date'
        })
    )

    invoice_id = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'min': '0'
    }))

    type = forms.ChoiceField(choices=TYPE_CHOICES, widget=forms.Select())

    amount = forms.DecimalField(widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }), min_value=Decimal('0.00'))

    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select())

    class Meta:
        model = Payments
        fields = ('customer', 'payment_date', 'invoice_id', 'type', 'amount', 'status')


class SupportManagerForm(BSModalForm):
    class Meta:
        model = SupportManager
        fields = ('name', 'email', 'avatar', 'phone_number', 'skype', 'website')


class UserForm(BSModalForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'is_active', 'is_superuser')


class BalanceForm(BSModalForm):
    class Meta:
        model = Balance
        fields = ('balance',)
