from django.contrib import admin
from core.models import Colaborador


class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'data_criacao', 'uf', 'cidade', 'cargo', 'unidade')
    list_filter = ('nome', 'data_criacao', 'uf', 'cidade', 'cargo', 'unidade',)


admin.site.register(Colaborador)
