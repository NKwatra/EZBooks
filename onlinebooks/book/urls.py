from django.urls import path
from . import views

app_name = 'book'
urlpatterns = [
    path('ajax', views.search, name='ajax'),
    path('<str:category>', views.category, name='category'),
]