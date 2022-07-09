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
    brand = forms.CharField(max_length=128)
    color = forms.CharField(max_length=128)
    release_year = forms.CharField(max_length=4)
    model = forms.CharField(max_length=128)

    class Meta:
        model = Car
        fields = ['brand', 'color', 'release_year', 'model']


class CompanyCreationForm(forms.ModelForm):
    name = forms.CharField(max_length=128)
    services = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    email = forms.EmailField(required=True)

    class Meta:
        model = Company
        fields = ['name', 'services', 'email']
