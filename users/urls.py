from django.urls import path
from users import views

app_name = "users"
urlpatterns = [
    path("login_user/", views.login_user, name="login_user"),
]
