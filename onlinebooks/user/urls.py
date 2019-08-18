from django.urls import path
from . import views

app_name='user'

urlpatterns = [
    path('ajax/update/<int:user_id>', views.ajaxUpdate, name='personal'),
    path('profile/<int:user_id>', views.profile, name='profile'),
]