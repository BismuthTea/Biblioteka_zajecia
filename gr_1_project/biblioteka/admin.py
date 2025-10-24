from django.contrib import admin

from .models import Genre, Author, Book, Person, Position

admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Person)
admin.site.register(Position)