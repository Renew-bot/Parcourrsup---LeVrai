from django.shortcuts import render
from .models import Bonjour

def Bonjour_view(request):
    tasks=Bonjour.objects.all()
    return render (request, 'Appli_ParcourSup/index.html', {'tasks': tasks})
