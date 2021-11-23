from django import forms
from .models import UserProfile
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-dark rounded-0 profile-form-input'
            self.fields[field].label = False


class UserTestProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'default_phone_number', 'default_postcode',
                   'default_town_or_city', 'default_street_address1',
                   'default_street_address2', 'default_county',
                   'default_country',)

    def __init__(self, *args, **kwargs):
        """
        Test Form
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'fname': 'First Name',
        }

      #  self.fields['default_postcode'].widget.attrs['autofocus'] = True
       # self.fields['user'].disabled = True
      #  for field in self.fields:
      #      self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
       #     self.fields[field].label = False
