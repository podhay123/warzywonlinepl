from django.shortcuts import render
from main.forms import ProductForm
from main.models import Product, Profile, ProductToSell
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def main(request):
    return render(request, "main/index.html", {})

# @login_required(login_ur)
def sell(request):
    form = ProductForm
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            user_object = User.objects.get(username=request.user.username)
            user_profile = Profile.objects.get(user=user_object)
            item.save()
            user_profile.user_products.add(item)

            print(item)
        else:
            print("???")
    return render(request, "main/seller_page.html", {"form": form} )


def all_products(request):
    products = Product.objects.all()

    return render(request, "main/all_products.html", {"products": products})


def product_page(request, id):
    product = ProductToSell.objects.get(product_id=id)

#     return render(request, "main/product_page.html", {"product": product})


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
