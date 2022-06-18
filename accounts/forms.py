from django import forms

from .models import Car, Auction, Service


class CarCreationForm(forms.ModelForm):
    brand = forms.CharField(max_length=128)
    color = forms.CharField(max_length=128)
    release_year = forms.CharField(max_length=4)
    model = forms.CharField(max_length=128)

    class Meta:
        model = Car
        fields = ['brand', 'color', 'release_year', 'model']


class AuctionCreationForm(forms.ModelForm):
    chosen_service = forms.ModelChoiceField(queryset=Service.objects.all())

    class Meta:
        model = Auction
        fields = ['chosen_service']
