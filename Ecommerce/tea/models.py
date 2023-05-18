from django.db import models

# Create your models here.
class Person(models.Model):
    name  = models.CharField(max_length=255)
    email  = models.EmailField(max_length=255)
    subject  = models.CharField(max_length=255)
    message = models.TextField()

class Product(models.Model):
    discription = models.TextField()
    upload_img = models.ImageField(upload_to='product/')