from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Product

# Create your views here.


def index(request):
    return render(request, 'plans/index.html', {})


def product_list(request, pk):
    products = get_object_or_404(Product, pk=pk)
    return render(request, 'plans/product_list.html', {'products': products})
