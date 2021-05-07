
from django.urls import path
from .import views


urlpatterns = [

    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('delievery', views.delievery, name='delievery'),
    path('cataloge', views.cataloge, name='cataloge'),
    path('basket', views.basket, name='basket'),
]