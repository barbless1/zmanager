#models.py permet de créer des tables au sein de la base de donnée MySQL

#Pour (re)créer la table "zoo" de la BDD : python manage.py makemigrations && python manage.py migrate 

from django.db import models

class Animal(models.Model):   #Le premier modèle défini est celui de l'animal. 
    NomAnimal = models.CharField(max_length=200)
    Espece = models.CharField(max_length=200, default='Undefined')
    DateNaissance = models.DateField(default=1970-1-1)
    DateArriveeZoo = models.DateField(default=1970-1-1)
    DateDepartZoo = models.DateField(default=1970-1-1)
    Age = models.IntegerField()
    RegimeAlimentaire = models.CharField(max_length=200, default='Undefined')
    class Meta:
        db_table = "zoo_animal"  # IMPORTANT : correspond au nom exact de la table, ça générait une erreur sinon
class Soigneur(models.Model): 
    Nom = models.CharField(max_length=200, default='tartempion')
    Prenom = models.CharField(max_length=200, default='tartempion')
    Role = models.IntegerField(default=0)

class Vaccin(models.Model):
    IdVaccin = models.BigIntegerField(default='0000')
    NomVaccin = models.CharField(max_length=200)

class Visite(models.Model):
    IdVisite = models.AutoField(primary_key=True)
    DateDerniereVisite = models.DateField(null=True, blank=True)
    DateDernierVaccin = models.DateField(null=True, blank=True)
    DateDerniereEchographie = models.DateField(null=True, blank=True)
    Pathologie = models.CharField(max_length=32, null=True, blank=True)
    DescriptionVisite = models.CharField(max_length=255, null=True, blank=True)
    Prenom = models.ForeignKey('Soigneur', on_delete=models.CASCADE)
    IdVaccin = models.ForeignKey('Vaccin', on_delete=models.SET_NULL, null=True, blank=True)

class Accidents(models.Model):
    DateAccident = models.DateField(default=1970-1-1)
    Commentaire = models.CharField(max_length=200, default='Undefined')
