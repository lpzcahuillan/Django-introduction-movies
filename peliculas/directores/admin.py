from django.contrib import admin
from .models import Director, Pelicula

class PeliculaInline(admin.TabularInline):
    model = Pelicula
    extra = 0

class DirectorAdmin(admin.ModelAdmin):
    inlines = [PeliculaInline]

admin.site.register(Director, DirectorAdmin)
admin.site.register(Pelicula)
