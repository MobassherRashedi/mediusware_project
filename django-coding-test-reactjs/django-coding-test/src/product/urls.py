from django.urls import path,include
from django.views.generic import TemplateView

from product.views.product import CreateProductView,ProductListView,ProductFilterView,CreateTestProduct
from product.views.variant import VariantView, VariantCreateView, VariantEditView

from .router import router

app_name = "product"

urlpatterns = [
    # Variants URLs
    path('variants/', VariantView.as_view(), name='variants'),
    path('variant/create', VariantCreateView.as_view(), name='create.variant'),
    path('variant/<int:id>/edit', VariantEditView.as_view(), name='update.variant'),

    # Products URLs
    path('create/', CreateProductView.as_view(), name='create.product'),
    path('list/', ProductListView.as_view(), name='product_list'),
    path('search/', ProductFilterView.as_view(), name='product_filter_list'),
    path(r'api/', include(router.urls)),
    
    # product create test
    path('create/test/', CreateTestProduct, name='create_product'),

]
