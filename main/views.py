from django.shortcuts import render
from main.forms import ProductForm
from main.models import Product
from django.contrib.auth import authenticate, login


# Create your views here.
def main(request):
    return render(request, "main/index.html", {})


def sell(request):
    form = ProductForm
    if request.method == "POST":
        product = request.POST.get("product")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        print(product)
        print(price)
        print(quantity)
        print("???")
    return render(request, "main/seller_page.html", {"form": form})


def all_products(request):
    products = Product.objects.all()

    return render(request, "main/all_products.html", {"products": products})


def product_page(request, name):
    product = Product.objects.get(name=name)

    return render(request, "main/product_page.html", {"product": product})


def search_product(request):
    if request.method == "POST":
        searched = request.POST.get("searched")
        products = Product.objects.filter(name__contains=searched)
        return render(
            request,
            "main/search_product.html",
            {
                "searched": searched,
                "products": products,
            },
        )
    else:
        return render(request, "main/search_product.html", {})
