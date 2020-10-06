from rest_framework import serializers
from .models import ProductModel


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        fields = ['id', 'title', 'description', 'price', 'author', 'author_id', 'category']

    def create(self, validated_data):
        return ProductModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('author', instance.price)
        instance.save()
        return instance
