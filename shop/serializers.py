from rest_framework import serializers
from .models import ProductModel


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    price = serializers.DecimalField(decimal_places=2, max_digits=10)
    image = serializers.ImageField()
    author = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return ProductModel.objects.create(**validated_data)
