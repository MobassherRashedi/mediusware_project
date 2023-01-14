from rest_framework import serializers
from .models import Product, Variant, ProductImage, ProductVariant, ProductVariantPrice

from rest_framework import serializers
from .models import Product, Variant, ProductImage, ProductVariant, ProductVariantPrice

class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ('id', 'title', 'description', 'active')

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'product', 'file_path')

class ProductVariantSerializer(serializers.ModelSerializer):
    variant = VariantSerializer()
    class Meta:
        model = ProductVariant
        fields = ('id', 'variant_title', 'variant', 'product')

class ProductVariantPriceSerializer(serializers.ModelSerializer):
    product_variant_one = ProductVariantSerializer()
    product_variant_two = ProductVariantSerializer()
    product_variant_three = ProductVariantSerializer()
    class Meta:
        model = ProductVariantPrice
        fields = ('id', 'product_variant_one', 'product_variant_two', 'product_variant_three', 'price', 'stock', 'product')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'sku', 'description')

'''/*
from rest_framework import serializers
from .models import Product, Variant, ProductImage, ProductVariant, ProductVariantPrice

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    class Meta:
        model = ProductImage
        fields = '__all__'

class ProductVariantSerializer(serializers.ModelSerializer):
    variant = serializers.PrimaryKeyRelatedField(queryset=Variant.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    class Meta:
        model = ProductVariant
        fields = '__all__'

class ProductVariantPriceSerializer(serializers.ModelSerializer):
    product_variant_one = serializers.PrimaryKeyRelatedField(queryset=
*/'''