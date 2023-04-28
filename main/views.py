from django.shortcuts import render
from main.models import Product


# Create your views here.
def main(request):
    return render(request, "main/index.html")


def product_page(request):
    product = Product.objects.all()
    return render(request, "main/product_page.html", {"product": product})
