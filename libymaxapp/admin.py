from django.contrib import admin
from .models import Genre, Book
# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Genre , GenreAdmin)
admin.site.register(Book , BookAdmin)