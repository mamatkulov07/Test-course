from allauth.account.forms import SignupForm
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import UserProfile


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=100, label=_('first_name'))
    last_name = forms.CharField(label=_('last_name'))
    last_login = forms.IntegerField(label=_('last_login'))
    date_joined = forms.IntegerField(label=_('date_joined'))
    role = forms.CharField(max_length=100, label=_('role'))
    phone_number = forms.CharField(max_length=20, label=_('Phone Number'))

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']

        phone_number = phone_number.replace(" ", "")

        if len(phone_number) != 9 or not phone_number.isdigit():
            raise ValidationError(_('Invalid phone number format. Please use 11-digit format without spaces'))

        return phone_number

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)

        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        role = self.cleaned_data['role']
        last_login = self.cleaned_data['last_login']
        date_joined = self.cleaned_data['date_joined']
        phone_number = "+996 " + self.cleaned_data['phone_number']

        if hasattr(user, 'userprofile'):
            profile = user.userprofile
        else:
            profile = UserProfile(user=user)

        profile.first_name = first_name
        profile.last_name = last_name
        profile.role = role
        profile.last_login = last_login
        profile.date_joined = date_joined
        profile.phone_number = phone_number
        profile.save()

        return user