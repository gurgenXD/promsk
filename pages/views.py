from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import Http404
from pages.models import Page


class PageView(View):
    def get(self, request, page_slug):
        page = get_object_or_404(Page, slug=page_slug)
        parents = page.get_ancestors(ascending=False, include_self=False)

        context = {
            'page': page,
            'parents': parents,
        }
        if page.action == 'pages':
            return render(request, 'pages/default.html', context)
        if page.action == 'dropdown':
            return render(request, 'pages/dropdown.html', context)
        raise Http404
