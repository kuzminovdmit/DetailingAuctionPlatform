from django import forms


class CarCreationForm(forms.Form):
    brand = forms.CharField(max_length=128)
    color = forms.CharField(max_length=128)
    release_year = forms.CharField(max_length=4)
    model = forms.CharField(max_length=128)


class ServiceChoiceForm(forms.Form):
    chosen_service = forms.IntegerField()
