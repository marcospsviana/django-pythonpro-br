from djangopythonpro.autores.models import Autores
from typing import List


def listar_autores_ordenados() -> List[Autores]:
    """
    Lista autores ordenados por título
    :[return]: List(Autores)
    """
    return list(Autores.objects.order_by('titulo').all())
