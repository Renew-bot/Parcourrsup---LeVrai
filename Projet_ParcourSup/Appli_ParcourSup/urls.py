from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.Bonjour_view, name='Page Accueil'),  
    path('formations/', views.formations_view, name='liste_formations'),
    path('index/formations/page/ajouter/', views.ajouter_formation, name='ajouter_formation'),  
    path('formations/modifier/<int:pk>/', views.modifier_formation, name='modifier_formation'),  
    path('formations/supprimer/<int:pk>/', views.supprimer_formation, name='supprimer_formation'),  
    path('index/formations/page/', views.formations_view, name='formations_view'),
]
