from django.urls import path
from . import views

app_name='order'
urlpatterns = [
    path('new/<int:book_id>/<int:order_type>', views.newOrder, name='newOrder'),
    path('place/<int:book_id>/<int:type>', views.placeOrder, name='placeOrder'),
    path("cancel/<int:order_id>", views.cancelOrder, name='cancelOrder'),
]