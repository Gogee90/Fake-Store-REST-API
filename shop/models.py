from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ProductCategory(models.Model):
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='media')

    def __str__(self):
        return self.category


class ProductModel(models.Model):
    author = models.ForeignKey(User, related_name='products', on_delete=models.Model)
    category = models.ForeignKey(ProductCategory, on_delete=models.Model)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='media')
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CommentModel(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.Model)
    created_date = models.DateTimeField(auto_now=True)
