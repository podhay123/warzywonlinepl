from django.shortcuts import render
from main.forms import ProductForm
from main.models import Product, Profile, ProductToSell, Category
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


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
            item.seller = user_profile.user
            item.save()
            user_profile.user_products.add(item)

            print(item)
        else:
            print("???")
    return render(request, "main/seller_page.html", {"form": form})


def all_products(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    return render(request, "main/all_products.html", {"products": products, "categories": categories})


def products_category(request, category):
    categories = Category.objects.all()
    products = Product.objects.filter(category__name=category)

    return render(request, "main/all_products.html", {"products": products, "categories": categories})


def product_page(request, name):

    products_to_sell = ProductToSell.objects.filter(product__name=name)
    
    try:
        name = products_to_sell[0].product.name
    except:
        name = "Brak ofert wybranego produktu"
    return render(
        request,
        "main/product_page.html",
        {
            "products_to_sell": products_to_sell,
            "name": name,
        },
    )


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


@login_required()
def account(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    print(user_profile.user_products.all())
    return render(
        request,
        "main/account.html",
        {
            "user": user_object,
            "profile": user_profile,
            "products": user_profile.user_products.all(),
        },
    )
