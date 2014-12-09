from django.contrib import admin
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
	pass


admin.site.register(Producto, ProductoAdmin)