from django.shortcuts import render, get_object_or_404
from django.views import View
from news.models import News
from pages.models import Page


class NewsView(View):
    def get(self, request):
        news = News.objects.filter(is_active=True)
        parents = Page.objects.get(action='news').get_ancestors(ascending=False, include_self=False)

        context = {
            'news': news,
            'parents': parents,
        }
        return render(request, 'news/news.html', context)


class NewsDetailView(View):
    def get(self, request, news_slug):
        news_item = get_object_or_404(News, slug=news_slug)
        parents = Page.objects.get(action='news').get_ancestors(ascending=False, include_self=False)

        context = {
            'news_item': news_item,
            'parents': parents,
        }
        return render(request, 'news/news-detail.html', context)
