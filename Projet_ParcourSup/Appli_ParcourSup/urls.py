from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('index/', views.Bonjour_view, name='Page Accueil'),  
    path('formations/', views.formations_view, name='liste_formations'),
    path('index/formations/page/ajouter/', views.ajouter_formation, name='ajouter_formation'),  
    path('formations/modifier/<int:pk>/', views.modifier_formation, name='modifier_formation'),  
    path('formations/supprimer/<int:pk>/', views.supprimer_formation, name='supprimer_formation'),  
    path('index/formations/page/', views.formations_view, name='formations_view'),
    path('profil/', views.profil_view, name='profil_view'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', LogoutView.as_view(next_page='profil_view'), name='logout'),
    path('pas_connecte/', views.pas_connecte_view, name='pas_connecte'),
    path('formations/postuler/<int:pk>/', views.postuler_formation, name='postuler_formation'),
    path('formations/accepter/<int:formation_pk>/<int:candidat_pk>/', views.accepter_candidature, name='accepter_candidature'),
    path('formations/refuser/<int:formation_pk>/<int:candidat_pk>/', views.refuser_candidature, name='refuser_candidature'),
    path('candidature/details/<int:pk>/', views.details_candidature, name='details_candidature'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)