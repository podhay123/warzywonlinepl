from django.shortcuts import render
from main.forms import ProductForm


# Create your views here.
def main(request):
    return render(request, "main/index.html", {})


def sell(request):
    form = ProductForm

    return render(request, "main/seller_page.html", {"form": form})
