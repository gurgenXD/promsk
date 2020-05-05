from django.urls import path
from orders import views


urlpatterns = [
    path('add_order/', views.OrderView.as_view(), name='order'),
]