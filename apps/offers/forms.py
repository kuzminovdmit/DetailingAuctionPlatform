from django import forms

from .models import Offer


class OfferCreationForm(forms.ModelForm):
    cost = forms.IntegerField()
    order_datetime_end = forms.DateTimeField(input_formats=['%d.%m.%Y, %H:%M'])

    class Meta:
        model = Offer
        fields = ['cost', 'order_datetime_end']
