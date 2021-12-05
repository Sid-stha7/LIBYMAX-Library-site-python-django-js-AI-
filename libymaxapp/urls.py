from django import urls
from  django.urls import  path
from . import views

urlpatterns = [
    path('', views.landing),
    path("register", views.register, name="register"),
    path("login",views.login, name="login"),
    path("logout",views.logout,name="logout")

]
