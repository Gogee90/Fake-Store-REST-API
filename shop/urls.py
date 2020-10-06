from django.urls import path
from .views import ProductView, ProductDetailView

app_name = "products"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('products/', ProductView.as_view()),
    path('products/<int:pk>', ProductDetailView.as_view())
  ]
