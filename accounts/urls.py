from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('myprofile/', views.myprofile, name='myprofile'),
    # path('login/', views.Login.as_view(), name='login'),
    # path('signup/', views.Signup.as_view(), name='signup'),

]
