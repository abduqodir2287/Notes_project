from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("home/", views.home_page, name="home"),
    path("notes/", views.index, name="todo"),
    path("login_password/", views.login_password, name="login_password"),
    path("del/<str:item_id>", views.remove, name="delete"),
    path("register/", views.homework_register, name="register"),
    path("", views.homework_login, name="home_login"),
    path("home_page", views.homework_home_page, name="home_page"),
    path("hello/", views.hello, name="hello"),
    path("main/", views.main, name="main"),
    path("experiment/", views.experiment, name="experiment"),
    path("photo/", views.get_photo, name='photo'),
    path("avatar/", views.avatar, name='avatar'),
    path('work/', views.work, name='work')
]
