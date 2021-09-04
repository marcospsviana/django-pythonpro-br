import pytest

from model_mommy import mommy
from django.urls import reverse
from djangopythonpro.demo.models import Videos
from djangopythonpro.django_assertions import assert_contains


@pytest.fixture
def videos(db):
    return mommy.make(Videos)


@pytest.fixture
def resp(client, videos):
    return client.get(reverse("demo:video", args=(videos.slug,)))


@pytest.fixture
def resp_not_found(client, videos):
    return client.get(reverse("demo:video", args=(videos.slug + "ferrou",)))


def test_status_code_not_found(resp_not_found, videos):
    assert resp_not_found.status_code == 404


def test_status_code(resp, videos):
    assert resp.status_code == 200


def test_titulo_video(resp, videos):
    assert_contains(resp, videos.titulo)


def test_conteudo_video(resp, videos):
    assert_contains(resp, videos.video_id)
