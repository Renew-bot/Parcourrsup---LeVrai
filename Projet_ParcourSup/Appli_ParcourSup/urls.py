from django.urls import path
from . import views

urlpatterns = [
    path('', views.Bonjour_view, name='Bonjour')
]