from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        print(username,email,password)
        user = User(username=username,email=email,password=password)
        user.save()
        return redirect("login")
    return render(request,"demo/register.html")
def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        print(email,password)
        username = User.objects.get(email=email).username
        user = auth.authenticate(username=username,password=password)
        print(user)
        return redirect("register")
    return render(request,"demo/login.html")        