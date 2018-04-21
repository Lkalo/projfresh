
from django.conf.urls import include, url
from django.contrib import admin

from apps.users import views

urlpatterns = [
    url(r'^register$', views.register, name='register'),
    url(r'^do_register$', views.do_register, name='do_register'),
    url(r'^login$', views.login, name='login'),
    url(r'^user_center_info$', views.user_center_info, name='user_center_info'),
    url(r'^user_center_order$', views.user_center_order, name='user_center_order'),
    url(r'^user_center_site$', views.user_center_site, name='user_center_site'),
    url(r'^order_comment$', views.order_comment, name='order_comment'),
]
