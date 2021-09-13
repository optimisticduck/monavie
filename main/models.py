from django.db import models

# Create your models here.
class ContactUs_T(models.Model):
    customerName = models.CharField(max_length=30)
    customerMessage = models.CharField(max_length=100)


class Orders_T(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    number = models.IntegerField(max_length=30)
    cusaddress = models.CharField(max_length=50)
    delins = models.CharField(max_length=60)
    totalCost = models.CharField(max_length=80)
    itemsOrdered = models.CharField(max_length=80)