from django.shortcuts import render, get_object_or_404
from django.views import View
from products.models import *
from pages.models import Page
from orders.forms import OrderForm


class CategoriesView(View):
    def get(self, request):
        categories = Category.objects.all()
        
        context = {
            'categories': categories,
        }
        return render(request, 'products/categories.html', context)


class CategoryView(View):
    def get(self, request, category_slug):
        category = get_object_or_404(Category, slug=category_slug)

        categories = category.get_descendants(include_self=True)
        products = Product.objects.filter(category__in=categories)

        parents = category.get_ancestors(ascending=False, include_self=False)

        context = {
            'category': category,
            'products': products,
            'parents': parents,
        }
        return render(request, 'products/category.html', context)


class ProductView(View):
    def get(self, request, category_slug, product_slug):
        product = get_object_or_404(Product, slug=product_slug)

        category = product.category
        parents = category.get_ancestors(ascending=False, include_self=False)

        images = product.images.all()
        slider_elems = [(nmb, val) for nmb, val in enumerate(images)]

        similar_products = product.similars_for.all()[:8]

        order_form = OrderForm()

        context = {
            'product': product,
            'slider_elems': slider_elems,
            'similar_products': similar_products,
            'category': category,
            'parents': parents,
            'order_form': order_form,
        }
        return render(request, 'products/product.html', context)
