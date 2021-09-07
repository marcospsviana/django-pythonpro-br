from django.shortcuts import render
from django.urls import reverse
from djangopythonpro.autores import facade_autores


def detalhes(request, slug):
    context = facade_autores.listar_autores_ordenados()
    return render(
        reverse("base:home", context)
    )
