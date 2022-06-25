from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, Car


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class CarCreationForm(forms.ModelForm):
    brand = forms.CharField(max_length=128)
    color = forms.CharField(max_length=128)
    release_year = forms.CharField(max_length=4)
    model = forms.CharField(max_length=128)

    class Meta:
        model = Car
        fields = ['brand', 'color', 'release_year', 'model']
