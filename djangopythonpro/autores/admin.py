from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from djangopythonpro.autores.models import Autores


@admin.register(Autores)
class AutoresAdmin(OrderedModelAdmin):
    list_display = ["titulo", "descricao", "move_up_down_links"]
    populated_fields = {"slug": ("titulo",)}
