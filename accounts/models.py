from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    location = models.CharField(max_length = 455)
    education =  models.CharField(max_length = 455)
    age = models.IntegerField()
    email = models.EmailField(unique = True)
  
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['age','location','education','username']