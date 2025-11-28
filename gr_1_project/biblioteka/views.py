from django.shortcuts import render #domyślny render nie jest potrzebny w widokach API
from rest_framework import status # zbiór statusów HTTP np. 404notfound, 200ok, 201created
from rest_framework.decorators import api_view # dekorator do definiowania widoków API
from rest_framework.response import Response # klasa do tworzenia odpowiedzi API
from .models import Book, Osoba, Stanowisko
from .serializers import BookSerializer, OsobaSerializer, StanowiskoSerializer

# określamy dostępne metody żądania dla tego endpointu
@api_view(['GET', "POST"])
# metoda otrzymuje dokorator api_view, który przekształca ją w widok API
def book_list(request):
    """
    Lista wszystkich obiektów modelu Book.
    """
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True) # many=True informuje serializer, że będzie serializować wiele obiektów i utworzy listę
        return Response(serializer.data, status=status.HTTP_200_OK) # zwracamy odpowiedź z danymi oraz statusem 200 OK
    
    elif request.method == 'POST': # tworzenie nowego obiektu Book
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) # zwracamy odpowiedź z danymi oraz statusem 201 Created

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # zwracamy odpowiedź z błędami walidacji oraz statusem 400 Bad Request
# nie potrzeba else bo intendacja

@api_view(['GET', 'PUT', 'DELETE']) # określamy dostępne metody żądania dla tego endpointu
def book_detail(request, pk): # pk to parametr ścieżki URL, identyfikujący primary key obiektu Book

    """
    :param request: obiekt DRF Request
    :param pk: id obiektu Book
    :return: Response (with status and/or object/s data)
    """
    try: # try except obsługuje błąd 404 Not Found, gdy obiekt o podanym pk nie istnieje
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 

    """
    Zwraca pojedynczy obiekt typu Book.
    """
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED) # statusem 202 Accepted albo 200 OK zależy od API designu
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', "POST", "DELETE"])
def osoba_detail(request, pk):

    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OsobaSerializer(osoba)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = OsobaSerializer(osoba, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', "POST"])
def osoba_list(request):
    if request.method == 'GET':
        osoby = Osoba.objects.all()
        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = OsobaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def osoba_search(request):
    # W GET używamy query_params (to, co w URL po znaku ?)
    search_criteria = request.query_params.get('search_criteria', None)

    if search_criteria:

        osoby = Osoba.objects.filter(last_name__icontains=search_criteria)
    else:
        osoby = Osoba.objects.all()

    serializer = OsobaSerializer(osoby, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
   
@api_view(['GET', "POST", "DELETE"])
def stanowisko_detail(request, pk):
    try:
        stanowisko = Stanowisko.objects.get(pk=pk)
    except Stanowisko.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StanowiskoSerializer(stanowisko)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = StanowiskoSerializer(stanowisko, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        stanowisko.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', "POST"])
def stanowisko_list(request):
    if request.method == 'GET':
        stanowiska = Stanowisko.objects.all()
        serializer = StanowiskoSerializer(stanowiska, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = StanowiskoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)