from django.shortcuts import render
from .models import Product


def all_products(request):
    """A view show all products page, including sortingand search queries  """
    prodcuts = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)