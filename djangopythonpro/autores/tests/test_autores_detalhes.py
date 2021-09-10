import pytest
from django.shortcuts import reverse

from djangopythonpro.autores.models import Autores
from djangopythonpro.django_assertions import assert_contains
from model_bakery import baker


@pytest.fixture
def autor(db):
    autor_return = baker.make(Autores)
    return autor_return


@pytest.fixture
def resp(client, autor):
    resp_autor = client.get(reverse("autores:detalhes", kwargs={"slug": autor.slug}))
    return resp_autor


def test_titulos_autor(resp, autor):
    assert_contains(resp, autor.titulo)


def test_descricao_autor(resp, autor):
    assert_contains(resp, autor.descricao)


def test_slug_autor(resp, autor):
    assert_contains(resp, autor.slug)
