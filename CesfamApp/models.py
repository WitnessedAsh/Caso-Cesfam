from django.db import models

# Create your models here.

class Production(models.Model):
  nombre = models.Charfield(max_length=64)
  categoria = models.Charfield(max_length=32
  precio = models.IntegerField()
                               
                               
     def __str__(self):
           return f'{self.nombre} ->{self.precio}'                    
                               
    
