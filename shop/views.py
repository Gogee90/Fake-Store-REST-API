from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ProductModel, ProductCategory, CommentModel
from .serializers import ProductSerializer
from rest_framework import status
from django.http import Http404


class ProductView(APIView):
  def get(self, request):
    products = ProductModel.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(APIView):
  def get_product(self, pk):
    try:
      return ProductModel.objects.get(pk=pk)
    except ProductModel.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    product = self.get_product(pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    product = self.get_product(pk)
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    product = self.get_product(pk)
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
