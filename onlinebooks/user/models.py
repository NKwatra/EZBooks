from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

app_name = 'Customer'

#   Model for a customer(user)
#   user: a foreign key reference to django's build in user model
#   profile_pic: a dp  for the user
#   address: the address of user where products are to be delivered
#   mobile_nos: mobile number of the user
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="images/")
    address = models.TextField()
    mobile_no = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.user.email

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.customer.save()

