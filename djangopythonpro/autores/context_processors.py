from djangopythonpro.autores import facade


def listar_autores(request):
    return {"AUTORES": facade.listar_autores_ordenados()}
