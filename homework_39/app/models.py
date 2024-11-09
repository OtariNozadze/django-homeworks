from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Category'

class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    description = models.TextField()
    isbn = models.CharField(max_length=13, unique=True)
     
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Book'