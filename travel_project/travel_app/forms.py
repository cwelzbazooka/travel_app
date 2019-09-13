from django import forms
from .models import Single_Localisation

class LocalisationForm(forms.ModelForm):
    class Meta:
        model = Single_Localisation
        fields = ['title', 'address','len_of_stay', 'description']