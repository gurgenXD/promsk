from django.urls import path
from feedback import views


urlpatterns = [
    path('add_message/', views.FeedBackView.as_view(), name='feedback'),
    path('add_call/', views.CallBackView.as_view(), name='callback'),
]