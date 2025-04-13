from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.drink_menu, name='drink_menu'),
    path('order/', views.order, name='order'),
]