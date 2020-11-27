from django.contrib import admin
from .models import ProductModel, CommentModel, ProductCategory, Cart
# Register your models here.

admin.site.register(ProductModel)
admin.site.register(CommentModel)
admin.site.register(ProductCategory)
admin.site.register(Cart)
