from django.urls import reverse
from djangopythonpro.django_assertions import assert_contains
import pytest
from djangopythonpro.demo.models import Videos
from model_bakery import baker


@pytest.fixture
def videos(db):
    videos_all = baker.make(Videos, _quantity=3)
    return videos_all


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
        assert_contains(resp, f"{v.slug}")
