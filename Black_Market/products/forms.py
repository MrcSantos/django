from django.db import models
from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
from .models import seller
from .models import product


class seller_form(ModelForm):
    class Meta:
        model = seller
        fields = ['username', 'password', 'thumbnail']


class product_form(ModelForm):
    class Meta:
        model = product
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['thumbnail', 'title', 'description', 'price', 'valuta']
