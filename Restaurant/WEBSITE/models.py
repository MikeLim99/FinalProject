import uuid
from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length = 100)
    price = models.FloatField()
    description = models.CharField(max_length = 200, default = '', blank = True, null= True)
    image = models.ImageField(upload_to='uploads/product/')

    def __str__(self):
        return self.name

class Reservation(models.Model):
    name = models.CharField(max_length = 100)
    phone =models.IntegerField()
    email = models.CharField(max_length = 100)
    type_of_celebration = models.CharField(max_length = 50)
    your_date = models.CharField(max_length = 50)
    your_time = models.CharField(max_length = 50)
    number_of_person = models.CharField(max_length = 50)
    random_number = models.CharField(max_length=36, default=uuid.uuid4, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name= 'created')

    def __str__(self):
        return self.name

class CustomerFeedback(models.Model):
    cx_name=models.CharField(max_length=50)
    cx_email=models.CharField(max_length=50)
    cx_feedback=models.CharField(max_length=200)

    def __str__(self):
        return self.cx_name
