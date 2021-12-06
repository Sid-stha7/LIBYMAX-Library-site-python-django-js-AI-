from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Book , Genre , Data
from django.db.models import Q
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
      'bestseller_books': bestseller_books ,  'articles' : articles
    }
   

    return render(request, 'index.html' , context)
    
def home(request):

    recommended_books = Book.objects.filter(recommended=True)
    bestseller_books = Book.objects.filter(bestseller=True)
    return render(request, 'book.html', {'recommended_books': recommended_books, 'bestseller_books': bestseller_books})


def browse(request):

   
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(book_author__icontains=q) | Q(book_title__icontains=q) | Q(book_genre__icontains=q))
        data = Data.objects.filter(multiple_q)
        
    else:
        data = Data.objects.all()



    recommended_books = Book.objects.filter(recomended=True)
    bestseller_books = Book.objects.filter(bestseller=True)
    context = {
        'recommended_books': recommended_books ,  'data': data
    }
   
    return render(request, 'browse.html' , {
        'recommended_books': recommended_books ,  'data': data
    })


# def genre_detail(request , slug):
#     genre = Genre.objects.get(slug=slug)
#     return render(request, 'book.html')



def book_detail(request , slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'book.html', {'book': book})

    
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


    