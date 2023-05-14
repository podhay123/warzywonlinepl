from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def login_user(request):
    print("login \n l")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main:main")
        else:
            messages.success(request, ("There Was An Error Logging In, Try Again..."))
            return redirect("users:login")

    else:
        return render(request, "users/authenticate/login.html", {})


def logout_user(request):
    print("HALO HALO \n HALO HALO HALO")
    logout(request)
    messages.success(request, ("Wylogowano poprawnie!"))
    return redirect("main:main")


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Zarejestrowano poprawnie!"))
            return redirect("main:main")
    else:
        form = UserCreationForm()

    return render(
        request,
        "users/authenticate/register_user.html",
        {
            "form": form,
        },
    )
