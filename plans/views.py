from django.shortcuts import render
from .models import Product


# Create your views here.


def index(request):
    return render(request, 'plans/index.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'plans/product_list.html', {'products': products})


def create_product(request):
    return render(request, 'plans/create_product.html')
