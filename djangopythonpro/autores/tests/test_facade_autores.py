import pytest
from model_bakery import baker
from djangopythonpro.autores.models import Autores
from djangopythonpro.autores import facade_autores


@pytest.fixture
def autores(db):
    return [baker.make(_model=Autores, titulo=t) for t in Autores.objects.all()]


def test_listar_autores_ordenados(autores):
    assert (
        list(sorted(autores, key=lambda autor: autor.slug))
        == facade_autores.listar_autores_ordenados()
    )
