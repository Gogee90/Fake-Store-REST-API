from django.contrib import admin
from .models import ProductModel, CommentModel, ProductCategory
# Register your models here.

admin.site.register(ProductModel)
admin.site.register(CommentModel)
admin.site.register(ProductCategory)
