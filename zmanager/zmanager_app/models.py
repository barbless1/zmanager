from django.db import models


class Animal(models.Model):                     #Le premier modèle défini est celui de l'animal. Il fait référence au modèle de la bdd "mysql_template.sql"
    name = models.CharField(max_length=200)
    species = models.CharField(max_length=200)
    age = models.IntegerField()
    arrival_date = models.DateField()

    def __str__(self):
        return self.name
