from django import forms
from .models import SmartLinks
from profiles.models import User


class SmartLinksForm(forms.ModelForm):
    customer = forms.ModelChoiceField(queryset=User.objects.all().order_by('email'), widget=forms.Select(),
                                      empty_label=None)

    smart_link = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control m-input m-input--square', 'placeholder': 'Smart Link'})
    )

    class Meta:
        model = SmartLinks
        fields = ('customer', 'smart_link')
