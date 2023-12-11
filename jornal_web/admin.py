from django.contrib import admin
from .models import Postador, Publicacao, Tags

# Register your models here.
admin.site.register(Postador)
admin.site.register(Publicacao)
admin.site.register(Tags)