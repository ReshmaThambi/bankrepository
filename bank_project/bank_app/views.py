from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .models import District
from .models import Branch


# Create your views here.
def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=uname, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        uname = request.POST['username']
        password = request.POST['password']
        cpass = request.POST['password1']

        if password == cpass:
            if User.objects.filter(username=uname).exists():
                messages.info(request, "username already exist")
                return redirect('register')
            else:
                user = User.objects.create_user(username=uname, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, "password not matched")
            return redirect('register')
        # return redirect('/')
    return render(request, 'register.html')


def welcome(request):
    return render(request, "welcome.html")


def form(request):
    obj = District.objects.all()
    obj1 = Branch.objects.all().filter()
    return render(request, "form.html", {'result': obj, 'result1': obj1})


def msgbox(request):
    return render(request, "msgbox.html")

