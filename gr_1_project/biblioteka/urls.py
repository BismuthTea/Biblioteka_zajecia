# plik biblioteka/urls.py

from django.urls import path, include
from . import views

urlpatterns = [
    path('books/', views.book_list),
    path('books/<int:pk>/', views.book_detail), # rodzaj zmiennej, nazwa zmiennej    book detail pokazuje zmienną pk
    path('osoby/', views.osoba_list),
    path('osoby/<int:pk>/', views.osoba_detail),
    path('osoby/search/', views.osoba_search),
    path('stanowiska/', views.stanowisko_list),
    path('stanowiska/<int:pk>/', views.stanowisko_detail),

    path('welcome/', views.welcome_view),
    path("html/osoby/", views.osoba_list_html, name="osoba-list"),
]