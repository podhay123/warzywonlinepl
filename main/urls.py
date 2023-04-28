from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("", views.main, name="main"),
    path("product_page/", views.product_page, name="product_page"),
]
