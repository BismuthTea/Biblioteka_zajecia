from django.contrib import admin

from .models import Genre, Author, Book, Osoba , Stanowisko

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'Stanowisko', 'entry_date')
    list_filter = ['Stanowisko', 'entry_date']

class StanowiskoAdmin(admin.ModelAdmin):
    list_filter = ('name', 'description')

admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Osoba , PersonAdmin,)
admin.site.register(Stanowisko, StanowiskoAdmin)