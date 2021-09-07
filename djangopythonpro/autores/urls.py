from django.urls import path

from djangopythonpro.autores.views import autores

app_name = "autores"
urlpatterns = [
    path("<slug:slug>", autores, name="detalhes"),
]
