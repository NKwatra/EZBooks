from django.urls import path
from . import views

app_name = 'authenticate'

urlpatterns = [
    path('signup', views.sign_up, name='sign_up'),
]