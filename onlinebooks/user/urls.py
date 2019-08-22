from django.urls import path
from . import views

app_name='user'

urlpatterns = [
    path('ajax/update/<int:user_id>', views.ajaxUpdate, name='personal'),
    path('profile/<int:user_id>', views.profile, name='profile'),
    path('password/change', views.password_change, name='password_change'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('wishlist/remove', views.remove_wishlist, name='removeWishlist'),
]