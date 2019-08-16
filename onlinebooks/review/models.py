from django.db import models
from book.models import Book
from user.models import Customer
from django.core.validators import MinValueValidator, MaxValueValidator

#   Model for review
#       rating: rating given by the user for the given book
#       review: comments given by the user
#       book: the book on which review ws given
#       user: the user who has given review
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review = models.TextField()

    def __str__(self):
        return self.review
