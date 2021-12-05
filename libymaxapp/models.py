from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField("Genre",max_length=100)
    slug = models.SlugField( max_length=100)
    def __str__(self):
        return self.name



class Book(models.Model):
    title = models.CharField("Title",max_length=100)
    slug = models.SlugField(max_length=100)
    coverImage = models.ImageField(upload_to='covers/',blank=True , null = True) 
    author = models.CharField("Author",max_length=100)
    description = models.TextField("Description")
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
    pdf = models.FileField(upload_to='pdf/',blank=True , null = True)
    recomended= models.BooleanField(default=False)
    fiction_books = models.BooleanField(default=False)
    nonfiction_books = models.BooleanField(default=False)
    bestseller = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Data(models.Model):
    book_title = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    book_genre = models.CharField(max_length=100)

    def __str__(self):
        return self.book_title