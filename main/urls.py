from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("", views.main, name="main"),
    path("sell/", views.sell, name="sell"),
    path("product_page/", views.product_page, name="product_page"),
    path("search_product/", views.search_product, name="search_product"),
]
