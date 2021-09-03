import pytest

# from django.test import Client
from django.urls import reverse

from djangopythonpro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse("base:home"))


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, "<title>Python Pro Fodásticos</title>")


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}">home</a>')
