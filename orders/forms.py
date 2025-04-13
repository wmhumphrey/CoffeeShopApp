from django import forms
from .models import DrinkType, Flavor, Milk, SIZE_CHOICES, PastryType

class OrderForm(forms.Form):
    drink_type = forms.ModelChoiceField(
        queryset=DrinkType.objects.all(),
        label='Drink Type',
    )
    size = forms.ChoiceField(
        choices=SIZE_CHOICES,
        label='Size',
    )
    flavor = forms.ModelChoiceField(
        queryset=Flavor.objects.all(),
        label='Flavor',
    )
    milk = forms.ModelChoiceField(
        queryset=Milk.objects.all(),
        label='Milk',
    )
    extra_shots = forms.IntegerField(
        min_value=0,
        initial=0,
        label='Extra Shots',
    )
    whip_cream = forms.BooleanField(
        required=False,
        label='Whipped Cream',
    )