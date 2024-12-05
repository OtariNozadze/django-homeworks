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
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    picture = models.ImageField(upload_to='books/', default=None, null=True, blank=True)
     
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Book'