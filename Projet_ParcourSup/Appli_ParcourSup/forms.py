from django import forms
from .models import Formation
from django.contrib.auth.forms import UserCreationForm

class FormationForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = ['nom', 'description', 'duree', 'etablissement']
