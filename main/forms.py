from django import forms
from django.forms import ModelForm
from main.models import ProductToSell


class ProductForm(ModelForm):
    class Meta:
        model = ProductToSell
        fields = "__all__"
