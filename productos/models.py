from django.db import models


class Producto(models.Model):
	nombre = models.CharField(max_length=60)


	def __unicode__(self):
		return self.name

