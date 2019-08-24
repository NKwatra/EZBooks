from django.urls import path
from . import views


app_name = 'authenticate'

urlpatterns = [
    path('', views.auth, name='authenticate'),
    path('signup', views.sign_up, name='sign_up'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('ajax/', views.checkEmail, name='checkEmail'),
    path('activate/<str:uidb64>/<str:token>', views.activate, name='activate'),
    path('password/reset', views.password_reset, name='passwordReset'),
    path('password/change/<str:uidb64>/<str:token>', views.password_change, name='passwordChange'),
]