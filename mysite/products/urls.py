from django.conf.urls import url, include
from django.contrib import admin
from products import views

urlpatterns = [
    url(r'^product/(?P<product_id>\w+)/$', views.product, name='product'),
    url(r'^new_items/$', views.new_items, name='new_items'),
    url(r'^discounts/$', views.discounts, name='discounts'),
    url(r'^products_men/$', views.products_men, name='products_men'),
    url(r'^products_women/$', views.products_women, name='products_women'),
    url(r'^products_children/$', views.products_children, name='products_children'),
]
