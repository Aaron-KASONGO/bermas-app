from django.db import models

# Create your models here.
class Site(models.Model):
    nom = models.CharField(max_length=30)
    adresse = models.TextField()

class SousReseaux(models.Model):
    nom = models.CharField(max_length=30)
    adresse = models.TextField()
    adresse_ip = models.CharField(max_length=20)
    site = models.ForeignKey('Site', on_delete=models.CASCADE)

class Equipement(models.Model):
    nom = models.CharField(max_length=30)
    port = models.CharField(max_length=10)
    sousReseaux = models.ForeignKey('SousReseaux', on_delete=models.CASCADE)