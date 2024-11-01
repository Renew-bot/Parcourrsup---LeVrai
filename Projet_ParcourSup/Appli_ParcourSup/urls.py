from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

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
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)