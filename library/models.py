from django.contrib.auth.models import User
from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=20)


class Book(models.Model):
    isbn = models.CharField(primary_key=True, max_length=13)
    name = models.CharField(max_length=20)
    sub_name = models.CharField(max_length=50)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT)
    authors = models.ManyToManyField(User)
    price = models.IntegerField()
    pages = models.IntegerField()
    release_date = models.DateField()
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    update_date = models.DateTimeField(auto_now=True, editable=False)
