from django import forms
from .models import Osoba

# przykładowy formularz dla modelu Osoba
class OsobaForm(forms.ModelForm):
    class Meta:
        model = Osoba
        fields = ['first_name', 'last_name', 'sex', 'stanowisko']  # pola do formularza