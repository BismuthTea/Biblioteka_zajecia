# plik biblioteka/urls.py

from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
    path('books/', views.book_list),
    path('books/<int:pk>/', views.book_detail), # rodzaj zmiennej, nazwa zmiennej    book detail pokazuje zmienną pk
    path('books/update_delete/<int:pk>/', views.book_update_delete),
    path('osoby/', views.osoba_list),
    path('osoby/<int:pk>/', views.osoba_detail),
    path('osoby/search/', views.osoba_search),
    path('stanowiska/', views.stanowisko_list),
    path('stanowiska/<int:pk>/', views.stanowisko_detail),

    path('welcome/', views.welcome_view),
    path("html/osoby/", views.osoba_list_html, name="osoba-list"),
    path("html/osoby/<int:id>/", views.osoba_detail_html, name="osoba-detail"),
    path("html/osoby/dodaj/", views.osoba_create_html, name="osoba-create"),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', views.user_login, name='user-login'),
    path('logout/', views.user_logout, name='user-logout'),
]
