from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ProductModel, ProductCategory, CommentModel
from .serializers import ProductSerializer


class ProductView(APIView):
    def get(self, request):
        products = ProductModel.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({"products": serializer.data})

    def post(self, request):
        serializer = request.data.get['products']
        if serializer.is_valid(raise_exception=True):
            product_saved = serializer.save()
        return Response({"success": "Product '{}' created successfully".format(product_saved.title)})
