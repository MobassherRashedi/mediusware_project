from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView

from product.models import Product,Variant,ProductImage,ProductVariant,ProductVariantPrice



class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name='products/list.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True)
        product_variants_list = {}
        for variant in variants:
            all_variant = list(variant.product_variants.all().values_list('variant_title').distinct())
            product_variants_list[variant.title] = all_variant

        context['product_variants'] = product_variants_list
        return context

class ProductFilterView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/list.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(ProductFilterView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True)
        product_variants_list = {}
        for variant in variants:
            all_variant = list(variant.product_variants.all().values_list('variant_title').distinct())
            product_variants_list[variant.title] = all_variant

        context['product_variants'] = product_variants_list
        return context

    def get_queryset(self):  # new
        products = Product.objects.all().distinct()
        title = self.request.GET.get("title")
        variant_title = self.request.GET.get("variant")
        date = self.request.GET.get("date")
        max_price = self.request.GET.get("price_to")
        min_price = self.request.GET.get("price_from")

        if  max_price == None or max_price=="":
            max_price = 999999
        else:
            max_price = int(self.request.GET.get("price_to"))

        if  min_price == None or min_price=="":
            min_price = 0
        else:
            min_price = int(self.request.GET.get("price_from"))
        if title:
            products = products.filter(title__icontains=title)
        if variant_title:
            products = products.filter(variants__variant_title__icontains=variant_title)
        if min_price or max_price:
            products = products.filter(product_variant_prices__price__range=(min_price, max_price))
        if date:
            products = products.filter(created_at__date=date).distinct()

        queryset = products
     
        return queryset




