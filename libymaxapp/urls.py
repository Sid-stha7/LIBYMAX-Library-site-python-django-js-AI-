from django import urls
from  django.urls import  path
from . import views

urlpatterns = [
    path('register', views.register, name="register"),
    path("login",views.login, name="login"),
    path("logout",views.logout,name="logout"),
    path('browse', views.browse, name="browse"),
    path('book/<str:slug>', views.book_detail, name="book_detail"),
    path('genre/<str:slug>', views.book_detail, name = 'book_detail'),
    path('', views.landing),
]
