import pytest
from model_mommy import mommy
from djangopythonpro.autores.models import Autores
from djangopythonpro.autores import facade


@pytest.fixture
def autores(db):
    return [mommy.make(Autores, titulo=t) for t in "Antes Depois".split()]


def test_listar_autores_ordenados(autores):
    assert (
        list(sorted(autores, key=lambda autor: autor.titulo))
        == facade.listar_autores_ordenados()
    )
