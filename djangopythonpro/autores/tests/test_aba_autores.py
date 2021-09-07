# import pytest

# # from django.test import Client
# from django.urls import reverse
# from djangopythonpro.autores.models import Autores
# from djangopythonpro.django_assertions import assert_contains
# from model_mommy import mommy


# @pytest.fixture
# def autores(db):
#     mommy.make(Autores, 2,)


# @pytest.fixture
# def resp(client, autores):
#     resp_autor = client.get(reverse("base:home"))
#     return resp_autor


# def test_titulos_autores(resp, autores):
#     for autor in autores:
#         assert_contains(resp, f'href="{autor}"')
