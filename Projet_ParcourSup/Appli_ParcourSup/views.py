from .models import Bonjour
from django.shortcuts import render, redirect, get_object_or_404
from .models import Formation
from .forms import FormationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def Bonjour_view(request):
    tasks = Bonjour.objects.all()
    return render(request, 'Appli_ParcourSup/index.html', {'tasks': tasks})

def formations_view(request):
    formations = Formation.objects.all()
    return render(request, 'Appli_ParcourSup/Formations.html', {'formations': formations})

def ajouter_formation(request):
    if request.method == 'POST':
        form = FormationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('liste_formations')
    else:
        form = FormationForm()
    return render(request, 'Appli_ParcourSup/ajouter_formation.html', {'form': form})

def modifier_formation(request, pk):
    formation = get_object_or_404(Formation, pk=pk)
    if request.method == 'POST':
        form = FormationForm(request.POST, request.FILES, instance=formation)
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

@login_required(login_url='pas_connecte')
def profil_view(request):
    utilisateur = request.user
    profile, created = Profile.objects.get_or_create(user=utilisateur)
    return render(request, 'Appli_ParcourSup/profil.html', {'utilisateur': utilisateur, 'profile': profile})

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user, status=form.cleaned_data['status'])
            login(request, user)
            return redirect('Page Accueil')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'Appli_ParcourSup/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Page Accueil')
    else:
        form = AuthenticationForm()
    return render(request, 'Appli_ParcourSup/login.html', {'form': form})

def pas_connecte_view(request):
    return render(request, 'Appli_ParcourSup/pas_connecte.html')

@login_required(login_url='pas_connecte')
def postuler_formation(request, pk):
    formation = get_object_or_404(Formation, pk=pk)

    if request.method == 'POST':
        if request.user in formation.candidats.all():
            messages.warning(request, 'Vous avez déjà postulé à cette formation.')
        else:
            formation.candidats.add(request.user)
            messages.success(request, 'Vous avez postulé à la formation avec succès !')
            return redirect('liste_formations')

    return render(request, 'Appli_ParcourSup/postuler_formation.html', {'formation': formation})