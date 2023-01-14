from rest_framework import routers
from .product_api_view import ProductViewSet, VariantViewSet, ProductImageViewSet, ProductVariantViewSet, ProductVariantPriceViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'variants', VariantViewSet)
router.register(r'productimages', ProductImageViewSet)
router.register(r'productvariants', ProductVariantViewSet)
router.register(r'productvariantprices', ProductVariantPriceViewSet)

