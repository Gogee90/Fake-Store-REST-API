from .models import ProductModel, ProductCategory, CommentModel
from .serializers import (ProductSerializer, UserSerializer, CategorySerializer,
CommentSerializer)
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


class CommentView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        product = self.kwargs['product']
        return CommentModel.objects.filter(product=product)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CategoryView(generics.ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveAPIView):
  queryset = ProductCategory.objects.all()
  serializer_class = CategorySerializer

class ProductView(generics.ListCreateAPIView):
  queryset = ProductModel.objects.all()
  serializer_class = ProductSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

  def perform_create(self, serializer):
    serializer.save(author=self.request.user)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = ProductModel.objects.all()
  serializer_class = ProductSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                        IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
# legacy code
# class ProductDetailView(APIView):
#  def get_product(self, pk):
#    try:
#      return ProductModel.objects.get(pk=pk)
#    except ProductModel.DoesNotExist:
#      raise Http404
#
#  def get(self, request, pk, format=None):
#    product = self.get_product(pk=pk)
#    serializer = ProductSerializer(product)
#    return Response(serializer.data)
#
#  def put(self, request, pk, format=None):
#    product = self.get_product(pk)
#    serializer = ProductSerializer(product, data=request.data)
#    if serializer.is_valid():
#      serializer.save()
#      return Response(serializer.data)
#    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#  def delete(self, request, pk, format=None):
#    product = self.get_product(pk)
#    product.delete()
#    return Response(status=status.HTTP_204_NO_CONTENT)
