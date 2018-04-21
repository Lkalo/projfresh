from django.conf.urls import include, url
from django.contrib import admin

from apps.orders import views

urlpatterns = [
    url(r'^place_order$', views.place_order, name='place_order'),
]
