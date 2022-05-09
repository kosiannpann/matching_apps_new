from django.urls import path
from . import views

app_name = 'message'

urlpatterns = [
    path('message_history/', views.message_history, name='message_history'),
]
