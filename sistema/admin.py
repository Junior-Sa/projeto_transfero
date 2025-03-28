from django.contrib import admin

from sistema import models
# aqui fica o registro do usuario
@admin.register(models.Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'ativo',)

# aqu fica o registro do filme
@admin.register(models.Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'ano', 'studio', 'genero',)

@admin.register(models.Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome',)
