from rest_framework import serializers
from .models import ProductModel, ProductCategory
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):

  class Meta:
    model = ProductCategory
    fields = ['category', 'description', 'image']


class ProductSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.username')
  category = serializers.ReadOnlyField(source='category.category')
  author = serializers.ReadOnlyField(source='author.username')

  class Meta:
    model = ProductModel
    fields = ['id', 'title', 'description', 'price', 'author', 'author_id', 'category', 'created_date', 'owner', 'image', ]

  def create(self, validated_data):
    return ProductModel.objects.create(**validated_data)

  def update(self, instance, validated_data):
    instance.title = validated_data.get('title', instance.title)
    instance.description = validated_data.get('description', instance.description)
    instance.price = validated_data.get('price', instance.price)
    instance.save()
    return instance


class UserSerializer(serializers.ModelSerializer):
  products = serializers.PrimaryKeyRelatedField(many=True, queryset=ProductModel.objects.all())

  class Meta:
    model = User
    fields = ['id', 'username', 'products']
