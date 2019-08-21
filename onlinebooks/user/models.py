from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from book.models import Book

app_name = 'Customer'

#   Model for a customer(user)
#   user: a foreign key reference to django's build in user model
#   profile_pic: a dp  for the user
#   address: the address of user where products are to be delivered
#   mobile_nos: mobile number of the user
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    mobile_no = models.CharField(max_length=16, null=True)
    reviews = models.ManyToManyField(Book, through='review.Review', related_name='reviews')
    wishlist = models.ManyToManyField(Book, related_name='wishlist')
    orders = models.ManyToManyField(Book, through='order.Order', related_name='orders')


    def __str__(self):
        return self.user.email

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.customer.save()

