from django.http import HttpResponse
from django.shortcuts import render, redirect #domyślny render nie jest potrzebny w widokach API
from rest_framework import status # zbiór statusów HTTP np. 404notfound, 200ok, 201created
from rest_framework.decorators import api_view # dekorator do definiowania widoków API
from rest_framework.response import Response # klasa do tworzenia odpowiedzi API
from .models import Book, Osoba, Stanowisko
from .serializers import BookSerializer, OsobaSerializer, StanowiskoSerializer
from django.http import Http404, HttpResponse
from .forms import OsobaForm
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
        serializer = OsobaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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
@api_view(['GET'])
def osoba_search(request):
    # W GET używamy query_params (to, co w URL po znaku ?)
    search_criteria = request.query_params.get('search_criteria', None)

    if search_criteria:

        osoby = Osoba.objects.filter(last_name__icontains=search_criteria)
    else:
        osoby = Response(status=status.HTTP_400_BAD_REQUEST)

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
        serializer = StanowiskoSerializer(data=request.data)
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
    
    from django.http import HttpResponse
import datetime


def welcome_view(request):
    now = datetime.datetime.now()
    html = f"""
        <html><body>
        Witaj użytkowniku! </br>
        Aktualna data i czas na serwerze: {now}.
        </body></html>"""
    return HttpResponse(html)

def osoba_list_html(request):
    # pobieramy wszystkie obiekty Osoba z bazy poprzez QuerySet
    osoby = Osoba.objects.all()
    #return HttpResponse(osoby)
    #mapujemy dane do szablonu HTML i zwracamy odpowiedź
    return render(request,
                  "biblioteka/osoba/list.html",
                  {'osoby': osoby})

#jakaś praca tu była


def osoba_detail_html(request, id):
    # pobieramy konkretny obiekt Osoba
    try:
        osoba = Osoba.objects.get(id=id)
    except Osoba.DoesNotExist:
        raise Http404("Obiekt Osoba o podanym id nie istnieje")

    if request.method == "GET":
            return render(request,
                        "biblioteka/osoba/detail.html",
                        {'osoba': osoba})
    if request.method == "POST":
        osoba.delete()
        return redirect('osoba-list') 


def osoba_create_html(request):
    stanowiska = Stanowisko.objects.all()  # pobieramy listę stanowisk z bazy

    if request.method == "GET":
        return render(request, "biblioteka/osoba/create.html", {'stanowiska': stanowiska})
    elif request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        sex = request.POST.get('sex')
        stanowisko_id = request.POST.get('stanowisko')

        if first_name and last_name and sex and stanowisko_id:
            # pobieramy obiekt stanowiska
            try:
                stanowisko_obj = Stanowisko.objects.get(id=stanowisko_id)
            except Stanowisko.DoesNotExist:
                error = "Wybrane stanowisko nie istnieje."
                return render(request, "biblioteka/osoba/create.html", {'error': error, 'stanowiska': stanowiska})

            # tworzymy nową osobę
            Osoba.objects.create(
                first_name=first_name,
                last_name=last_name,
                sex=sex,
                Stanowisko=stanowisko_obj
            )
            return redirect('osoba-list')
        else:
            error = "Wszystkie pola są wymagane."
            return render(request, "biblioteka/osoba/create.html", {'error': error, 'stanowiska': stanowiska})
        
def osoba_create_django_form(request):
    if request.method == "POST":
        form = OsobaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('osoba-list')  
    else:
        form = OsobaForm()

    return render(request,
                  "biblioteka/osoba/create_django.html",
                  {'form': form})