from django import forms


class AccountCreationForm(forms.Form):
    # user = forms.
    auto = forms.CharField(max_length=128)
    color = forms.CharField(max_length=128)
    release_year = forms.CharField(max_length=4)
    model = forms.CharField(max_length=128)