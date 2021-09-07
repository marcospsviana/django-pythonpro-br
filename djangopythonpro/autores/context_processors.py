from djangopythonpro.autores import facade_autores


def listar_autores(request):
    return {"FODASTICOS": facade_autores.listar_autores_ordenados()}
