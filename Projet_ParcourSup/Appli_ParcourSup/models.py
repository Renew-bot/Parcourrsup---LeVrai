from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    image = models.URLField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.nom
    
class Profile(models.Model):
    STATUS_CHOICES = (
        ('etudiant', 'Étudiant'),
        ('ecole', 'École'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.user.username
