from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render
from product.models import Product,Variant,ProductImage,ProductVariant,ProductVariantPrice
import json


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


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from product.models import Product, ProductImage, ProductVariant, Variant, ProductVariantPrice



'''
def CreateTestProduct(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        # save product
        product = Product.objects.create(
            title=data['product_title'],
            sku=data['sku'],
            description=data['description']
        )

        # save product images
        for image in data['images']:
            ProductImage.objects.create(
                product=product,
                path=image['path']
            )

        # save product variants
        for variant in data['variants']:
            variant_obj = Variant.objects.get(id=variant['option'])
            product_variant = ProductVariant.objects.create(
                product=product,
                variant=variant_obj,
            )

            # save tags for product variant
            for tag in variant['tags']:
                product_variant.tags.add(tag)
            product_variant.save()

        # save product variant prices
        for variant_price in data['variantPrices']:
            ProductVariantPrice.objects.create(
                product_variant=product_variant,
                title=variant_price['title'],
                price=variant_price['price'],
                stock=variant_price['stock']
            )
        return JsonResponse({"status": "success"})
    else:
        return JsonResponse({"status": "error"})
'''
@csrf_exempt
def CreateTestProduct(request):
    if request.method == "POST":
        # data = request.body
        data = json.loads(request.body)
        # Create Product
        product = Product.objects.create(
            title=data['product_title'],
            sku=data['sku'],
            description=data['description']
        )
        
        # Create Product Image
        for image in data['images']:
            ProductImage.objects.create(
                product=product,
                file_path=image
            )

        # Create Product Variants
        for variant in data['variants']:
            Product_Variant_obj = Variant.objects.get(id=variant['option'])
            for tag in variant['tags']:
                ProductVariant.objects.create(
                    variant_title=tag,
                    variant=Product_Variant_obj,
                    product=product
                )

        # Create Product Variant Prices
        for variant_price in data['variantPrices']:
            ProductVariantPrice.objects.create(
                product_variant_one=ProductVariant.objects.filter(product=product,variant_title__icontains=variant_price['title'].split('/')[0])[0],
                product_variant_two=ProductVariant.objects.filter(product=product,variant_title__icontains=variant_price['title'].split('/')[1])[0],
                product_variant_three=ProductVariant.objects.filter(product=product,variant_title__icontains=variant_price['title'].split('/')[2])[0],
                price=variant_price['price'],
                stock=variant_price['stock'],
                product=product
            )
        
        return JsonResponse({"status": "success"})
    else:
        return JsonResponse({"status": "error"})
