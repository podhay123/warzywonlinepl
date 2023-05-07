from django.shortcuts import render
from main.forms import ProductForm
from main.models import Product


# Create your views here.
def main(request):
    return render(request, "main/index.html", {})


def sell(request):
    form = ProductForm

    return render(request, "main/seller_page.html", {"form": form})


def all_products(request):
    products = Product.objects.all()

    return render(request, "main/all_products.html", {"products": products})


def product_page(request, pk):
    product = Product.objects.get(id=pk)

    return render(request, "main/all_products.html", {"product": product})
