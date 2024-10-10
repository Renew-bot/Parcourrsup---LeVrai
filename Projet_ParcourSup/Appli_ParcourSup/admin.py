from django.contrib import admin
from .models import Etablissement, Formation

# Enregistrement des modèles dans l'interface d'administration
@admin.register(Etablissement)
class EtablissementAdmin(admin.ModelAdmin):
    list_display = ('nom', 'adresse', 'ville', 'site_web')  # Colonnes à afficher dans l'admin
    search_fields = ('nom', 'ville')  # Champs pour la recherche

@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ('nom', 'etablissement', 'duree')  # Colonnes à afficher dans l'admin
    search_fields = ('nom', 'etablissement__nom')  # Champs pour la recherche
    list_filter = ('etablissement',)  # Filtres dans l'admin
