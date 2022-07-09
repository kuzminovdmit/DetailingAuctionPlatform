from django import forms

from apps.accounts.models import Car

from .models import Auction, Service


class AuctionCreationForm(forms.ModelForm):
    service = forms.ModelChoiceField(queryset=Service.objects.all())
    duration_choice = forms.ChoiceField(choices=Auction.DURATION_CHOICES)

    class Meta:
        model = Auction
        fields = ['car', 'service', 'start_cost', 'duration_choice']

    def __init__(self, user, *args, **kwargs):
        super(AuctionCreationForm, self).__init__(*args, **kwargs)
        self.fields['car'] = forms.ModelChoiceField(queryset=Car.objects.filter(client__user=user))
