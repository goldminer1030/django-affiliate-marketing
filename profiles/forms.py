from django import forms
from django.contrib.auth.forms import (ReadOnlyPasswordHashField,
                                       UserChangeForm as BaseUserChangeForm)
from django.utils.translation import ugettext as _
from django.contrib.auth import authenticate
from django.contrib.auth.forms import SetPasswordForm

from .models import Profile, User


class SignUpForm(forms.ModelForm):

    # user fields
    email = forms.EmailField(
        label='Email Address',
        max_length=75,
        widget=forms.TextInput(attrs={'class': 'form-control m-input m-input--square', 'placeholder': 'Email Address'})
    )

    password = forms.CharField(
        max_length=50,
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control m-input m-input--square', 'placeholder': 'Password'})
    )

    # profile fields
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control m-input m-input--square', 'placeholder': 'First Name'})
    )

    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control m-input m-input--square', 'placeholder': 'Last Name'})
    )

    class Meta:
        model = User
        fields = (
            'email', 'password',
            'first_name', 'last_name'
        )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update({'autofocus': True})

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            # check if there is super user
            if User.objects.filter(is_superuser=True).count() == 0:
                user.is_superuser = True
                user.is_active = True
                print('%s %s is a super-user' % (user.first_name, user.last_name))
            user.save()

        return user


class NewUserForm(SignUpForm):
    is_superuser = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class': 'form-check-label'
    }), required=False)

    class Meta:
        model = User
        fields = (
            'email', 'password', 'first_name', 'last_name', 'is_superuser'
        )


class ProfileEditForm(forms.ModelForm):
    # user fields
    email = forms.EmailField(
        label='Email address',
        max_length=75,
        widget=forms.TextInput(attrs={'class': 'form-control m-input m-input--square', 'placeholder': 'Email Address'}),
        help_text='We\'ll never share your email with anyone else'
    )

    # profile fields
    username = forms.CharField(
        label='User Name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control m-input m-input--square', 'placeholder': 'Enter User Name'}),
        help_text='We\'ll never share your username with anyone else',
        required=False
    )

    phone_number = forms.CharField(
        label='Mobile Phone Number',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control m-input m-input--square', 'placeholder': 'Enter Phone Number'}),
        help_text='We\'ll never share your phone number with anyone else'
    )

    class Meta:
        model = Profile
        fields = ('email', 'username', 'phone_number')

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        self.email = self.instance.get_email()
        self.username = self.instance.username
        self.fields['email'].initial = self.email

    def clean_email(self):

        email = self.cleaned_data['email']

        if email == self.email:
            return email

        qs = User.objects.filter(email__iexact=email)
        if qs.count() > 0:
            raise forms.ValidationError(_('This email is already in use.'))
        return email

    def clean_username(self):

        username = self.cleaned_data['username']
        if username == '' or self.username == username:
            return username

        qs = Profile.objects.filter(username__iexact=username)
        if qs.count() > 0:
            raise forms.ValidationError(_('This username is already in use.'))
        return username


class LoginForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """
    username = forms.EmailField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control m-input', 'placeholder': 'Email',
                                      'autofocus': True, 'autocomplete': 'off'}),
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control m-input m-login__form-input--last',
                                          'placeholder': 'Password'})
    )

    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(email)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("This account is inactive. Please contact with affiliate manager to approve this account."),
    }

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                try:
                    user_temp = User.objects.get(email=username)
                except:
                    user_temp = None

                if user_temp is not None and user_temp.check_password(password):
                    self.confirm_login_allowed(user_temp)
                else:
                    raise forms.ValidationError(
                        self.error_messages['invalid_login'],
                        code='invalid_login',
                        params={'email': 'Email Address'},
                    )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        """
        Controls whether the given User may log in. This is a policy setting,
        independent of end-user authentication. This default behavior is to
        allow login by active users, and reject login by inactive users.

        If the given user cannot log in, this method should raise a
        ``forms.ValidationError``.

        If the given user may log in, this method should return None.
        """
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache


class UserChangeForm(BaseUserChangeForm):
    email = forms.EmailField(label=_('Email'), max_length=75)
    password = ReadOnlyPasswordHashField(label=_('Password'),
                                         help_text=_('Raw passwords are not stored, so there is no way to see '
                                                     "this user's password, but you can change the password "
                                                     'using <a href="password/">this form</a>.'))


class UserCreationForm(forms.ModelForm):
    email = forms.EmailField(label=_('Email'), max_length=75)
    password = forms.CharField(label=_('Password'),
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Password confirmation'),
                                widget=forms.PasswordInput,
                                help_text=_('Enter the same password as above, for verification.'))

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError(_("The two password fields didn't match."))
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class PasswordChangeForm(SetPasswordForm):
    """
    A form that lets a user change their password by entering their old
    password.
    """
    error_messages = dict(SetPasswordForm.error_messages, **{
        'password_incorrect': _("Your current password was entered incorrectly. Please enter it again."),
    })
    old_password = forms.CharField(
        label=_("Current password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autofocus': True}),
    )

    field_order = ['old_password', 'new_password', 'new_password2']

    def clean_old_password(self):
        """
        Validates that the old_password field is correct.
        """
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'],
                code='password_incorrect',
            )
        return old_password

    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs = {'class': 'form-control m-input m-input--square'}
        self.fields['new_password'].widget.attrs = {'class': 'form-control m-input m-input--square'}
        self.fields['new_password2'].widget.attrs = {'class': 'form-control m-input m-input--square'}
        self.fields['new_password'].help_text = ''
