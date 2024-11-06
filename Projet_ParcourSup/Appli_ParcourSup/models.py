from django.db import models
from django.contrib.auth.models import User

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

class Candidature(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    lettre_motivation = models.TextField()
    date_postulation = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=10, choices=[('en_attente', 'En attente'), ('acceptee', 'Acceptée'), ('refusee', 'Refusée')], default='en_attente')

    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.formation.nom}"