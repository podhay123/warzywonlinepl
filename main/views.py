from django.shortcuts import render
from main.forms import ProductForm
from main.models import Product


# Create your views here.
def main(request):
    return render(request, "main/index.html", {})


def sell(request):
    form = ProductForm

    return render(request, "main/seller_page.html", {"form": form})


def product_page(request):
    product = Product.objects.all()
    return render(request, "main/product_page.html", {"product": product})
