from django.db import models

# Create your models here.
class Order_T(models.Model):
    orderID = models.CharField(max_length=5, primary_key=True)
    customerName = models.CharField(max_length=30)
