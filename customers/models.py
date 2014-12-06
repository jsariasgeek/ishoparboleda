from django.db import models
from products.models import Product as Product




class User(models.Model):
	nombres = models.CharField(max_length=60)
	apellidos = models.CharField(max_length=60)
	telefono = models.CharField(max_length=15)
	email = models.EmailField()
	workshops = models.BooleanField(default=True)
	products = models.ManyToManyField(Product)
	notes = models.TextField()
	contactado = models.BooleanField(default=False)


	def __unicode__(self):
		return self.nombres + ' ' + self.apellidos

