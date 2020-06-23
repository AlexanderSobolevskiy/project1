from django.conf.urls import url, include
from django.contrib import admin
from score import views

urlpatterns = [
    url(r'^score/$', views.score, name='score'),
]
