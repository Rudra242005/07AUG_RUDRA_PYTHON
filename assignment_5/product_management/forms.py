from django import forms
from .models import *

class productForm(forms.ModelForm):
    class Meta:
        model = product_data
        fields = '__all__'
