from django import forms
from django.contrib.auth.forms import UserCreationForm

from apps.auctions.models import Service
from .models import User, Car, Company


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class CarCreationForm(forms.ModelForm):
    brand = forms.CharField(max_length=128, required=True)
    model = forms.CharField(max_length=128, required=True)
    color = forms.CharField(max_length=128, required=True)
    release_year = forms.CharField(max_length=4, required=True)

    class Meta:
        model = Car
        fields = ['brand', 'model', 'color', 'release_year']


class CompanyCreationForm(forms.ModelForm):
    name = forms.CharField(max_length=128, required=True)
    services = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    email = forms.EmailField(required=True)

    class Meta:
        model = Company
        fields = ['name', 'services', 'email']
