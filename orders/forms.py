from django import forms
from orders.models import *


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'email', 'phone', 'text')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Электронная почта'}),
            'phone': forms.TextInput(attrs={'class': 'form-control phone-input', 'placeholder': '+7 (___) ___-__-__'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Описание заказа'}),
        }