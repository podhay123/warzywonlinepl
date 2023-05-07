from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("", views.main, name="main"),
    path("sell/", views.sell, name="sell"),
    path("all_products/", views.all_products, name="all_products"),
    path("<int:pk>/", views.product_page, name="product_page"),
]
