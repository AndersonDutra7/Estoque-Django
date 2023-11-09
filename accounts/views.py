from django.shortcuts import render, redirect
from django.contrib import auth, messages


def user_login(request):
    if request.method == "POST":
        user = request.POST.get("username")
        password = request.POST.get("password")

        userVerify = auth.authenticate(request, username=user, password=password)
        print(userVerify)

        if userVerify == None:
            messages.info(request, "Usuário ou senha incorretos.")
            return redirect("login")
        else:
            auth.login(request, userVerify)
            return redirect("home")

    else:
        return render(request, "pages/login.html")


def register(request):
    return (request, "pages/register.html")
