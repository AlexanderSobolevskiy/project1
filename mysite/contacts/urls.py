from django.conf.urls import url, include
from django.contrib import admin
from contacts import views

urlpatterns = [
    url(r'^contacts/$', views.contacts, name='contacts'),
]