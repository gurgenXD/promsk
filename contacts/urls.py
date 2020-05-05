from django.urls import path
from contacts.views import *
from pages.models import Page


urlpatterns = [
    path('', ContactsView.as_view(), name='contacts'),
]
