from django.urls import path
from . import views

app_name='order'
urlpatterns = [
    path('new/<int:book_id>/<int:order_type>', views.newOrder, name='newOrder'),
]