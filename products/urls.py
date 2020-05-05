from django.urls import path
from products.views import *


urlpatterns = [
    path('', CategoriesView.as_view(), name='categories'),
    path('<category_slug>/', CategoryView.as_view(), name='category'),
    path('<category_slug>/<product_slug>/', ProductView.as_view(), name='product'),
]