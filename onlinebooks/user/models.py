from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

app_name = 'Customer'

#   Model for a customer(user)
#   user: a foreign key reference to django's build in user model
#   profile_pic: a dp  for the user
#   address: the address of user where products are to be delivered
#   mobile_nos: mobile number of the user
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="images/")
    address = ArrayField(models.TextField())
    mobile_no = models.CharField(max_length=15)

