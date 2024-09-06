from django import forms
from .models import Pun, Rating

class PunForm(forms.ModelForm):
    class Meta:
        model = Pun
        fields = ['text']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']
