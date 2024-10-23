from .models import Bonjour
from django.shortcuts import render, redirect, get_object_or_404
from .models import Formation
from .forms import FormationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def Bonjour_view(request):
    tasks = Bonjour.objects.all()
    return render(request, 'Appli_ParcourSup/index.html', {'tasks': tasks})

def formations_view(request):
    formations = Formation.objects.all()
    return render(request, 'Appli_ParcourSup/Formations.html', {'formations': formations})

def ajouter_formation(request):
    if request.method == 'POST':
        form = FormationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_formations')
    else:
        form = FormationForm()
    return render(request, 'Appli_ParcourSup/ajouter_formation.html', {'form': form})

def modifier_formation(request, pk):
    formation = get_object_or_404(Formation, pk=pk)
    if request.method == 'POST':
        form = FormationForm(request.POST, instance=formation)
        if form.is_valid():
            form.save()
            return redirect('liste_formations')
    else:
        form = FormationForm(instance=formation)
    return render(request, 'Appli_ParcourSup/modifier_formation.html', {'form': form})

def supprimer_formation(request, pk):
    formation = get_object_or_404(Formation, pk=pk)
    if request.method == 'POST':
        formation.delete()
        return redirect('liste_formations')
    return render(request, 'Appli_ParcourSup/supprimer_formation.html', {'formation': formation})

@login_required
def profil_view(request):
    utilisateur = request.user
    return render(request, 'Appli_ParcourSup/profil.html', {'utilisateur': utilisateur})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Page Accueil')
    else:
        form = UserCreationForm()
    return render(request, 'Appli_ParcourSup/signup.html', {'form': form})