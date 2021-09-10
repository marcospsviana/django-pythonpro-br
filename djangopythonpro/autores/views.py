from django.shortcuts import render
from djangopythonpro.autores import facade_autores


def detalhes(request, slug):
    autor = facade_autores.encontrar_autor(slug)
    return render(request, "autores/detalhes.html", {"autor": autor})

