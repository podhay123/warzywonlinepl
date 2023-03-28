from django.urls import path
from main_seller import views


app_name = "main_seller"
urlpatterns = [
    path("", views.main, name="main_seller"),
]
