from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

GENDER_CHOICES = (
    ('M', "M"),
    ("F", "F"),
    ("IT", "IT")
)


class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
    age = forms.IntegerField(required=True)

    class Meta:
        model = models.CustomUser
        fields = [
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'gender',
            'phone_number'
        ]

    def save(self, commit=True):
        user = super(CustomRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
