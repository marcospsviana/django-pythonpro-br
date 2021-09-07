from djangopythonpro.autores.models import Autores
from typing import List


def listar_autores_ordenados() -> List[Autores]:
    return list(Autores.objects.order_by("order").all())
