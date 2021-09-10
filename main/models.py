from django.db import models

# Create your models here.
class ContactUs_T(models.Model):
    customerName = models.CharField(max_length=30)
    customerMessage = models.CharField(max_length=100)
