from django.db import models

class Producto(models.Model):
    nombreproducto = models.CharField(max_length=150)
    costopresupuesto = models.CharField(max_length=150)
    costoreal = models.CharField(max_length=150)
    notaadicional=models.TextField(default="")

    def __str__(selft):
        return self.nombreproducto 
