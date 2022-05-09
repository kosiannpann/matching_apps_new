from django.urls import path
from . import views

app_name = 'plans'

urlpatterns = [
    path('', views.index, name="index"),
    path('product_list/', views.product_list, name='product_list'),
]
