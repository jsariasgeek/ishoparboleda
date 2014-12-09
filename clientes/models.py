from django.db import models
from productos.models import Producto as Producto




class Cliente(models.Model):
	nombres = models.CharField(max_length=60)
	apellidos = models.CharField(max_length=60)
	telefono = models.CharField(max_length=15)
	email = models.EmailField()
	workshops = models.BooleanField(default=True)
	productos = models.ManyToManyField(Producto)
	notas = models.TextField()
	contactado = models.BooleanField(default=False)


	def __unicode__(self):
		return self.nombres + ' ' + self.apellidos

