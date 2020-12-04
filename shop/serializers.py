from rest_framework import serializers
from .models import ProductModel, ProductCategory, CommentModel, Cart
from django.contrib.auth.models import User


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = CommentModel
        fields = ['author', 'author_id', 'text', 'created_date', 'product']

    def create(self, validated_data):
        return CommentModel.objects.create(**validated_data)


class CategorySerializer(serializers.ModelSerializer):

  class Meta:
    model = ProductCategory
    fields = ['id', 'category', 'description', 'image']


class ProductSerializer(serializers.ModelSerializer):
  category = ProductCategory()
  author = serializers.ReadOnlyField(source='author.username')

  class Meta:
    model = ProductModel
    fields = ['id', 'title', 'description', 'price', 'author', 'category_id', 'category', 'created_date', 'image', 'quantity']

  def create(self, validated_data):
    return ProductModel.objects.create(**validated_data)

  def update(self, instance, validated_data):
    instance.title = validated_data.get('title', instance.title)
    instance.description = validated_data.get('description', instance.description)
    instance.price = validated_data.get('price', instance.price)
    instance.image = validated_data.get('image', instance.image)
    instance.save()
    return instance


class UserSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=ProductModel.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'products']


class CartSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    product_id = ProductSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'username', 'date', 'product_id']


class CartCreateSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Cart
        fields = ['id', 'user', 'username', 'date', 'product_id']

    def set(self, validated_data):
        return Cart.objects.create(**validated_data)
