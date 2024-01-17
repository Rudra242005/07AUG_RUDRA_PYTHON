from django import forms
from .models import *

class coustomerForm(forms.ModelForm):
    class Meta:
        model=coustomer
        fields='__all__'

class contactForm(forms.ModelForm):
    class Meta:
        model=contact
        fields='__all__'