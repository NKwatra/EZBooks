from django.urls import path
from . import views

app_name = 'book'
urlpatterns = [
    path('<str:category>', views.category, name='category'),
    path('<str:category>/ajax', views.search, name='ajax'),
]