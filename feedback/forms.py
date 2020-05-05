from django import forms
from feedback.models import *


class CallBackForm(forms.ModelForm):
    class Meta:
        model = CallBack
        fields = ('phone', 'name')
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control phone-input', 'placeholder': 'Телефон'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
        }


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ('name', 'email_or_phone', 'text')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'email_or_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон или E-mail'}),
            'text': forms.Textarea(attrs={'class': 'form-control rounded-lg', 'placeholder': 'Текст сообщения', 'rows': 5}),
        }