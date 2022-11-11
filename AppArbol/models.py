from django.db import models

# Create your models here.


class familia (models.Model):
    
        nombre = models.CharField(max_length= 40)
        apellido = models.CharField(max_length= 40)
        nacimiento = models.DateField()
        hijos = models.IntegerField ()
        edad = models.IntegerField()

