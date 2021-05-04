from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'name',
            'min_price',
            'max_price',
            'url',
            'type'
        )
        widgets = {
            'name': forms.TextInput
        }
