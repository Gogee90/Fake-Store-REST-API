from django.urls import path, include
from .views import (ProductView, ProductDetailView, UserList, UserDetail,
CategoryView, CategoryDetailView, CommentView, CartView, CartDetailView,
CreateCartView, EveryCartView)

app_name = "products"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('products/', ProductView.as_view()),
    path('products/<int:pk>', ProductDetailView.as_view()),
    path('category/', CategoryView.as_view()),
    path('category/<int:pk>', CategoryDetailView.as_view()),
    path('comments/<int:product>', CommentView.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>', UserDetail.as_view()),
    path('carts/', EveryCartView.as_view()),
    path('carts/create', CreateCartView.as_view()),
    path('carts/<int:pk>', CartView.as_view()),
    path('carts/single/<int:pk>', CartDetailView.as_view()),
    path('dj-rest-auth/', include('dj_rest_auth.urls'))
  ]
