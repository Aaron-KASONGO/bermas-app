from django.db import models

# Create your models here.
class Site(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nom

class SousReseaux(models.Model):
    nom = models.CharField(max_length=30)
    site = models.ForeignKey('Site', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nom

class Equipement(models.Model):
    nom = models.CharField(max_length=30)
    adresse_ip = models.CharField(max_length=20)
    sousReseaux = models.ForeignKey('SousReseaux', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nom