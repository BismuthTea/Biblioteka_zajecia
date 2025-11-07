from django.contrib import admin

from .models import Genre, Author, Book, Person, Position

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'entry_date')
    list_filter = ['position', 'entry_date']

class StanowiskoAdmin(admin.ModelAdmin):
    list_filter = ('name', 'description')

admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Person, PersonAdmin,)
admin.site.register(Position, StanowiskoAdmin)