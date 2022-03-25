from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Book(models.Model):
    isbn = models.CharField(primary_key=True, max_length=13)
    name = models.CharField(max_length=20)
    sub_name = models.CharField(max_length=50)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT)
    authors = models.ManyToManyField(Author)
    price = models.IntegerField()
    pages = models.IntegerField()
    release_date = models.DateField()
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    update_date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f"{self.name} - {self.sub_name}"
