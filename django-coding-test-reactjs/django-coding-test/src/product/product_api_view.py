from rest_framework import viewsets
from product.models import Product, Variant, ProductImage, ProductVariant, ProductVariantPrice
from product.serializers import ProductSerializer, VariantSerializer, ProductImageSerializer, ProductVariantSerializer, ProductVariantPriceSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class VariantViewSet(viewsets.ModelViewSet):
    queryset = Variant.objects.all()
    serializer_class = VariantSerializer

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

class ProductVariantViewSet(viewsets.ModelViewSet):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer

class ProductVariantPriceViewSet(viewsets.ModelViewSet):
    queryset = ProductVariantPrice.objects.all()
    serializer_class = ProductVariantPriceSerializer
