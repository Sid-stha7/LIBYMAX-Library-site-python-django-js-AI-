from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Book
import requests

APIkey = 'ec7a9cfa19bc4ed297992f8a2ed2c8a0'
category = 'Books'

#function for rendering the main page 
def landing(request):
   

   #fetching of the news for the latest news section on landing page 
    url  = f'https://newsapi.org/v2/everything?q={category}&from=2021-11-30&sortBy=popularity&apiKey={APIkey}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    recommended_books = Book.objects.filter(recomended=True)
    bestseller_books = Book.objects.filter(bestseller=True)
    context = {
        'recommended_books': recommended_books, 'bestseller_books': bestseller_books ,  'articles' : articles
    }
   

    return render(request, 'index.html' , context)
    
def home(request):

    recommended_books = Book.objects.filter(recommended=True)
    bestseller_books = Book.objects.filter(bestseller=True)
    return render(request, 'book.html', {'recommended_books': recommended_books, 'bestseller_books': bestseller_books})


def browse(request):

    recommended_books = Book.objects.filter(recomended=True)
    bestseller_books = Book.objects.filter(bestseller=True)
    context = {
        'recommended_books': recommended_books, 'bestseller_books': bestseller_books 
    }
   
    return render(request, 'browse.html' , context)





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


    