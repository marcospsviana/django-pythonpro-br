from django.shortcuts import render

# from djangopythonpro.autores import facade_autores


def home(request):
    return render(request, "home.html", {})
