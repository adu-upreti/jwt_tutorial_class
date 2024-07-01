from django.db import models
from accounts.models import CustomUser

class Book(models.Model):
    name = models.CharField(max_length = 200)
    price = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(CustomUser,on_delete = models.CASCADE)


class Sook(models.Model):
    name = models.CharField(max_length = 200)
    price = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(CustomUser,on_delete = models.CASCADE)