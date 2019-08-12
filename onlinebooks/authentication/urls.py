from django.urls import path
from . import views


app_name = 'authenticate'

urlpatterns = [
    path('', views.auth, name='authenticate'),
    path('signup', views.sign_up, name='sign_up'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('activate/<str:uidb64>/<str:token>', views.activate, name='activate'),
]