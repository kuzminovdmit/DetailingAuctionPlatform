from django import forms

from .models import Auction, Service


class AuctionCreationForm(forms.ModelForm):
    chosen_service = forms.ModelChoiceField(queryset=Service.objects.all())
    start_cost = forms.IntegerField()
    duration_choice = forms.ChoiceField(choices=Auction.DURATION_CHOICES)

    class Meta:
        model = Auction
        fields = ['chosen_service', 'start_cost', 'duration_choice']
