from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

#   Model for book:
#       category: The genre of book eg entertainment, philosopy, non-fiction etc
#       cover_image: the front cover of the book
#       title: title of the book
#       author: name of the author
#       stock: number of copies left in stock
#       avg_rating: the average rating of book, calculated on basis of reviews
#       publisher: publishing house of book
#       no_of_pages: number of pages in the book
#       price: price of the book
#       description: a short description telling the synopsis of the book
class Book(models.Model):
    category = models.CharField(max_length=150)
    cover_image = models.ImageField(upload_to="images/books/")
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    stock = models.IntegerField(default=10)
    avg_rating = models.FloatField(default=3)
    publisher = models.CharField(max_length=200)
    no_of_pages = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField(default="No Information Available")

    def __str__(self):
        return self.title