from django.db import models

class Animal(models.Model):
    NomAnimal = models.CharField(max_length=200)
    Espece = models.CharField(max_length=200, default='Undefined')
    DateNaissance = models.DateField(default='1970-01-01')
    DateArriveeZoo = models.DateField(default='1970-01-01')
    DateDepartZoo = models.DateField(default='1970-01-01')
    Age = models.IntegerField()
    RegimeAlimentaire = models.CharField(max_length=200, default='Undefined')
    class Meta:
        db_table = "zoo_animal"  
        
class Soigneur(models.Model): 
    Nom = models.CharField(max_length=200, default='tartempion')
    Prenom = models.CharField(max_length=200, default='tartempion')
    Specialisation = models.CharField(max_length=200, default='tartempion')
    Age = models.IntegerField(default='0')


class Visite(models.Model):
    DateDerniereVisite = models.DateField(null=True, blank=True)
    DateDernierVaccin = models.DateField(null=True, blank=True)
    Pathologie = models.CharField(max_length=32, null=True, blank=True)
    DescriptionVisite = models.CharField(max_length=255, null=True, blank=True)
    Soigneur = models.CharField(max_length=32, default='Soigneur')
    Animal = models.ForeignKey('Animal', on_delete=models.CASCADE)

class Accidents(models.Model):
    DateAccident = models.DateField(default='1970-01-01')
    Commentaire = models.CharField(max_length=200, default='Undefined')
