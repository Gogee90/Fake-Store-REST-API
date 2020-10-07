from django.urls import path, include
from .views import ProductView, ProductDetailView, UserList, UserDetail

app_name = "products"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('products/', ProductView.as_view()),
    path('products/<int:pk>', ProductDetailView.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>', UserDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
  ]
