from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'plans/index.html')


def product_list(request):
    return render(request, 'plans/product_list.html')
