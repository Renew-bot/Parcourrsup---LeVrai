from .models import Bonjour
from django.shortcuts import render, redirect, get_object_or_404
from .models import Formation
from .forms import FormationForm

def Bonjour_view(request):
    tasks = Bonjour.objects.all()
    return render(request, 'Appli_ParcourSup/index.html', {'tasks': tasks})

def formations_view(request):
    formations = Formation.objects.all()  # Récupérer toutes les formations
    return render(request, 'Appli_ParcourSup/Formations.html', {'formations': formations})

def ajouter_formation(request):
    if request.method == 'POST':
        form = FormationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_formations')  # Rediriger vers la liste des formations
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
