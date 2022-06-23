from django import forms

from .models import Auction, Service


class AuctionCreationForm(forms.ModelForm):
    chosen_service = forms.ModelChoiceField(queryset=Service.objects.all())

    class Meta:
        model = Auction
        fields = ['chosen_service']
