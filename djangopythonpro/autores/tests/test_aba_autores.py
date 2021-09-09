import pytest

# from django.test import Client
from django.shortcuts import reverse
from djangopythonpro.autores.models import Autores
from djangopythonpro.django_assertions import assert_contains
from model_bakery import baker


@pytest.fixture
def autores(db):
    autores_all = baker.make(Autores, _quantity=2)
    return autores_all
    # return Autores.objects.order_by('order').all()


@pytest.fixture
def resp(client, autores):
    resp_autor = client.get(reverse("base:home"))
    return resp_autor


def test_titulos_autores(resp, autores):
    for autor in autores:
        assert_contains(resp, autor)
