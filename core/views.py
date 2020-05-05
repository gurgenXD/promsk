from django.shortcuts import render
from django.views import View
from core.models import Index
from news.models import News
from contacts.models import *


class IndexView(View):
    def get(self, request):
        index = Index.objects.first()

        index_categories = index.index_categories.all()[:6]
        index_products = index.index_products.all()[:8]

        index_news = News.objects.filter(is_active=True)[:4]

        addresses = Address.objects.all()
        phones = Phone.objects.all()
        emails = Email.objects.all()
        schedule = Schedule.objects.all()
        map_code = MapCode.objects.first()

        context = {
            'index_categories': index_categories,
            'index_products': index_products,
            'index_news': index_news,
            'addresses': addresses,
            'phones': phones,
            'emails': emails,
            'schedule': schedule,
            'map_code': map_code,
        }
        return render(request, 'core/index.html', context)