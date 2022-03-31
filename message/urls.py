from django.urls import path
from . import views


urlpatterns = [
    path('message_history/', views.message_history, name='message_history'),
]
