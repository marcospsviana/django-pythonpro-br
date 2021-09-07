from django.shortcuts import render
from django.urls import reverse
from djangopythonpro.autores import facade_autores


def autores(request):
    context = facade_autores.listar_autores_ordenados()
    return render(
        reverse("base:home", current_app=request.resolver_match.namespace),
        context=context,
    )
