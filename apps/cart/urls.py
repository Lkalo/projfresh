from django.conf.urls import include, url
from django.contrib import admin

from apps.cart import views

urlpatterns = [
    url(r'^cart$', views.cart, name='cart'),
]
