from django.db import models
from book.models import Book
from user.models import Customer
import datetime
from django.utils import timezone

class Order(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(Customer, on_delete= models.CASCADE)
    date_of_purchase = models.DateTimeField(auto_now_add=True)
    order_type = models.IntegerField(choices= [
        (1, "Rent"),
        (2, "Buy"),
    ])
    status = models.IntegerField(choices=[
        (1, "active"),
        (2, "inactive"),
    ], default=1)

    def __str__(self):
        return self.book.title + " -> " + self.user.user.first_name

    def allow_cancel(self):
        return timezone.now() - self.date_of_purchase < datetime.timedelta(hours=12)