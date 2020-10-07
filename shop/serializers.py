from rest_framework import serializers
from .models import ProductModel
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.username')

  class Meta:
    model = ProductModel
    fields = ['id', 'title', 'description', 'price', 'author', 'author_id', 'category', 'created_date', 'owner']

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
