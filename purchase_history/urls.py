from django.urls import path
from . import views

app_name = 'purchase_history'

urlpatterns = [
    path('purchase_history_list/', views.purchase_history_list,
         name='purchase_history_list'),
]
