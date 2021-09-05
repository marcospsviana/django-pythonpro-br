import pytest

# from django.test import Client
from django.urls import reverse
from model_mommy import mommy

from djangopythonpro.django_assertions import assert_contains
from djangopythonpro.autores.models import Autores


@pytest.fixture
def autores(db):
    return mommy.make(Autores, 2)


@pytest.fixture
def resp(client, autores):
    content = client.get(reverse("base:home"))
    return content


def test_title(resp, autores):
    for autor in autores:
        return assert_contains(resp, autor.titulo)
