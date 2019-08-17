from django.urls import path
from . import views

app_name = 'book'
urlpatterns = [
    path('ajax/wishlist', views.wishlist, name='wishlist'),
    path('ajax', views.search, name='ajax'),
    path('<str:category>', views.category, name='category'),
    path('detail/<int:book_id>', views.detail, name='detail'),
]