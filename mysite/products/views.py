from django.shortcuts import render
from products.models import *


def product(request, product_id):
    product = Product.objects.get(id=product_id)


    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)


    return render(request, 'products/product.html', locals())


def discounts(request):
    products = ProductImage.objects.filter(is_active=True, product__discount_items=True, product__is_active=True)
    products_men = products.filter(product__category__id=2)
    products_women = products.filter(product__category__id=1)
    products_children = products.filter(product__category__id=3)
    return render(request, 'products/discounts.html', locals())


def new_items(request):
    products = ProductImage.objects.filter(is_active=True, product__new_items=True, product__is_active=True)
    products_men = products.filter(product__category__id=2)
    products_women = products.filter(product__category__id=1)
    products_children = products.filter(product__category__id=3)
    return render(request, 'products/discounts.html', locals())


def products_men(request):
    products = ProductImage.objects.filter(is_active=True, product__is_active=True)
    products_men = products.filter(product__category__id=2)
    return render(request, 'products/products_men.html', locals())


def products_women(request):
    products = ProductImage.objects.filter(is_active=True, product__is_active=True)
    products_women = products.filter(product__category__id=1)
    return render(request, 'products/products_women.html', locals())


def products_children(request):
    products = ProductImage.objects.filter(is_active=True, product__is_active=True)
    products_children = products.filter(product__category__id=3)
    return render(request, 'products/products_children.html', locals())