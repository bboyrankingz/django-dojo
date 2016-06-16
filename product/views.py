from django.shortcuts import get_object_or_404, render

from models import Product


def index(request):
    products = Product.objects.order_by('-pub_date')[:5]
    return render(request, 'index.html', {'products': products})


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'detail.html', {'product': product})
