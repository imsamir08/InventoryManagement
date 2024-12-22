from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    dob = models.DateField()
    phone = models.BigIntegerField()
    registered_at = models.DateField(auto_now_add=True)
