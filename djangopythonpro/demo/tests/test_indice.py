from django.urls import reverse
from djangopythonpro.django_assertions import assert_contains
import pytest
from djangopythonpro.demo.models import Videos
from model_mommy import mommy


@pytest.fixture
def videos(db):
    return mommy.make(Videos, 3)


@pytest.fixture
def resp(client, videos):
    return client.get(
        reverse(
            "demo:indice",
        )
    )


def test_int_index(resp):
    assert resp.status_code == 200


def test_titulo_video(resp, videos):
    for v in videos:
        assert_contains(resp, v.titulo)


def test_link_video(resp, videos):
    for v in videos:
        assert_contains(resp, f'{v.slug}')
