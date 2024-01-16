from django import forms
from .models import *

class coustomerForm(forms.ModelForm):
    class Meta:
        model=coustomer
        fields='__all__'