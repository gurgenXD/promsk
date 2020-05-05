from django.shortcuts import render
from django.views import View
from contacts.models import *
from pages.models import Page


class ContactsView(View):
    def get(self, request):
        addresses = Address.objects.all()
        phones = Phone.objects.all()
        emails = Email.objects.all()
        schedule = Schedule.objects.all()
        map_code = MapCode.objects.first()
        socials = Social.objects.all()
        whatsapp = WhatsApp.objects.first()
        parents = Page.objects.get(action='contacts').get_ancestors(ascending=False, include_self=False)

        context = {
            'addresses': addresses,
            'phones': phones,
            'emails': emails,
            'schedule': schedule,
            'map_code': map_code,
            'socials': socials,
            'whatsapp': whatsapp,
            'parents': parents,
        }
        return render(request, 'contacts/contacts.html', context)