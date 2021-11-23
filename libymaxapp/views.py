from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth



def register(request):
    if request.method == 'POST':
        username = request.POST['name']   
        password = request.POST['password']
        email = request.POST['email']
        
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        print('user created')
       
    
    else:
        return render(request, 'login.html')
    
        

    