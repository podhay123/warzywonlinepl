from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")

            # return render(request, "main\\templates\\main\\index.html")
        else:
            messages.success(request, ("There Was An Error Loggin In, Try Again"))
            return redirect("login")
    else:
        return render(request, "users/authentication/login.html", {})
