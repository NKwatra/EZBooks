from django.urls import path
from . import views

app_name='review'
urlpatterns = [
    path('add/<int:book_id>', views.addReview, name='addReview'),
]