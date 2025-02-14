from django.contrib import admin
from .models import Animal, Noticia, Comentario, Adopcion
# Register your models here.
admin.site.register(Animal)
admin.site.register(Noticia)
admin.site.register(Comentario)
admin.site.register(Adopcion)