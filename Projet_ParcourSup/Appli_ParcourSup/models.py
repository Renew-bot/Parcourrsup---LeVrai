from django.db import models
from django.contrib.auth.models import AbstractUser

class Bonjour(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    is_completed=models.BooleanField(default=False)

class Etablissement(models.Model):
    nom = models.CharField(max_length=200)
    adresse = models.CharField(max_length=300)
    ville = models.CharField(max_length=100)
    site_web = models.URLField()

    def __str__(self):
        return self.nom

class Formation(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    duree = models.CharField(max_length=50)
    etablissement = models.CharField(max_length=50)

    def __str__(self):
        return self.nom