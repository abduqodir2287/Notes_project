from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TodoForms, LoginForms, Home_Login_Forms
from .models import Todo, Homework_Login
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.template import loader

def index(request):
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo")
    form = TodoForms()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO  LIST"
    }
    return render(request, "todo.html", page)

def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "Item removed !!!")
    return redirect("todo")

def login_password(request):
    if request.method == "POST":
        form = LoginForms(request.POST)
        if form.is_valid():
            form.save()
    form = LoginForms

    page = {
        "forms": form
    }
    return render(request, "login_site.html", page)

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login_password.html', {'error_message': 'invalid login'})

    return render(request, 'login_password.html')

def home_page(request):
    if request.user.is_authenticated:
        return render(request, 'welcome.html')
    else:
        return redirect('login')

def homework_register(request):
    if request.method == "POST":
        form = Home_Login_Forms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home_login")
    form = Home_Login_Forms()

    page = {
        "forms": form
    }
    return render(request, "homework_register.html", page)


def homework_login(request):
    obj = Homework_Login.objects.all()

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        for i in obj:
            if username == i.username and password == i.password:
                return redirect('todo')

        else:
            return render(request, 'homework_login.html', {'error_message': 'Invalid login'})

    return render(request, "homework_login.html")

def homework_home_page(request):
    temp = loader.get_template("welcome.html")
    return HttpResponse(temp.render())

def hello(request):
    temp = loader.get_template("hello.html")
    return HttpResponse(temp.render())


def main(request):
    temp = loader.get_template("main.html")
    return HttpResponse(temp.render())

def experiment(request):
    template = loader.get_template("experiment.html")
    return HttpResponse(template.render())


def get_photo(request):
    temp = loader.get_template("get_photo.html")
    return HttpResponse(temp.render())

def avatar(request):
    temp = loader.get_template("avatar.html")
    return HttpResponse(temp.render())

def work(request):
    data = [
        {
            "icon_class": "fab fa-twitter fa-3x",
            "target": 12400,
            "label": "Twitter Followers"
         },
        {
            "icon_class": "fab fa-youtube fa-3x",
            "target": 32500,
            "label": "Youtube Followers"
        },
        {
            "icon_class": "fab fa-facebook fa-3x",
            "target": 500,
            "label": "Facebook Followers"
        }
    ]
    context = {
        "data": data
    }

    return render(request, 'work.html', context)




