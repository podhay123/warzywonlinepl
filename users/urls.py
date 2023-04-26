from django.urls import path
from users import views

app_name = "users"
urlpatterns = [
    path("login_user/", views.login_user, name="login"),
    path("", views.logout_user, name="logout"),  # login_user/????
    path("register_user/", views.register_user, name="register"),
]
