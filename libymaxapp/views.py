from django.shortcuts import render
from django.contrib.auth.models import User, auth


def register(request):
    return render(request, "login.html")
    # if request.method == "POST":
    #     Fullname=request.POST['name'],
    #     email=request.POST['email'],        
    #     password=request.POST['pass'],                

    #     user= User.objects.create_user()
    #     else:
    #         return render(request, "login.html")    
