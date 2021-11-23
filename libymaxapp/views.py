from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        
        username = request.POST['username']   
        password = request.POST['password']
        email = request.POST['email']

       
        if User.objects.filter(username=username).exists():
            print("Username taken")
            return render(request, 'login.html')   
        else:
         user = User.objects.create_user(username=username, password=password, email=email)
         user.save()
         print('user created')
         return render(request, 'login.html')
    
    else:
        print("retry again")
        return render(request, 'login.html')
    
        
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("register")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('register')

    else:
        return render(request, 'login.html')

    