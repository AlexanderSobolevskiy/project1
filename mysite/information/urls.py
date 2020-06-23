from django.conf.urls import url, include
from django.contrib import admin
from information import views

urlpatterns = [
    url(r'^information/$', views.information, name='information'),
]