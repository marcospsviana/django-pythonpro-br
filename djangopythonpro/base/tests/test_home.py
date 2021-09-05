import pytest

# from django.test import Client
from django.urls import reverse
from djangopythonpro.autores.models import Autores
from djangopythonpro.django_assertions import assert_contains
from model_mommy import mommy


@pytest.fixture
def autores(db):
    return mommy.make(Autores, 2)


@pytest.fixture
def resp(client, autores):
    return client.get(reverse("base:home"))


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp, autores):
    assert_contains(resp, "<title>Python Pro Fodásticos</title>")


def test_home_link(resp, autores):
    for autor in autores:
        assert_contains(resp, autor)
