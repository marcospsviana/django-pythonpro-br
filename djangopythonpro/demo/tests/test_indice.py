from django.urls import reverse
from djangopythonpro.django_assertions import assert_contains
import pytest
from djangopythonpro.demo.models import Videos
import os
from django.settings import setup


os.environ.default("DJANGO_SETTINGS_MODULE", "djangopythonpro.settings")
setup()


@pytest.fixture
def videos(db):
    db_filter = Videos.objects.filter(id=1)
    return db_filter


@pytest.fixture
def resp(client, db):
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
        video_link = reverse("demo:video", args=(v.slug,))
        assert_contains(resp, f'href="{video_link}"')
