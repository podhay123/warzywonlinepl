from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("", views.main, name="main"),
    path("sell/", views.sell, name="sell"),
    path("products/", views.all_products, name="all_products"),
    path("products/<str:category>", views.products_category, name="products_category"),
    path("products/<str:name>/", views.product_page, name="product_page"),
    path("search_product/", views.search_product, name="search_product"),
    path("profil", views.account, name="account"),
]
