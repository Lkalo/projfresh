from django.conf.urls import include, url
from django.contrib import admin

from apps.goods import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^detail$', views.detail, name='detail'),
    url(r'^detail2$', views.detail2, name='detail2'),
    url(r'^list$', views.list, name='list'),
]
