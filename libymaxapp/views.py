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
    url  = 'https://newsapi.org/v2/everything?q=Books&sortBy=popularity&apiKey=ec7a9cfa19bc4ed297992f8a2ed2c8a0'
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

    recommended_books = Book.objects.filter(recomended=True)
    bestseller_books = Book.objects.filter(bestseller=True)
   
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(book_author__icontains=q) | Q(book_title__icontains=q) | Q(book_genre__icontains=q))
        data = Data.objects.filter(multiple_q)
        return render(request, 'browse.html' , {
          'data': data
    })
    else:
        data = Data.objects.all()
        return render(request, 'browse.html' , {
        'recommended_books': recommended_books ,  'data': data
    })

   
   
   





def book_detail(request , slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'book.html', {'book': book})


 # register and login

def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')    

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')

        else:
            messages.info(request,'password not matching..')    
            return redirect('register')
        return redirect('/')
        
    else:
        return render(request,'login.html')



def logout(request):
    auth.logout(request)
    return redirect('/')  