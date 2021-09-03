import pytest

# from model_mommy import mommy
from django.urls import reverse
from djangopythonpro.demo.models import Videos
from djangopythonpro.django_assertions import assert_contains


@pytest.fixture
def videos(db):
    video = Videos(
        slug="renzo", titulo="os fodásticos do python dev pro", video_id="a61p-g0yWts"
    )
    video.save()
    return video


@pytest.fixture
def resp(client, videos):
    return client.get(reverse("demo:video", args=("renzo",)))


def test_status_code(resp, videos):
    assert resp.status_code == 200


def test_titulo_video(resp, videos):
    # for v in videos:
    assert_contains(resp, videos.titulo)


def test_conteudo_video(resp, videos):
    assert_contains(resp, videos.video_id)


# @pytest.mark.parametrize(
#     "titulo",
#     {
#         "renzo": {
#             "slug": "renzo",
#             "titulo": "os fodásticos do python dev pro",
#             "video_id": "a61p-g0yWts",
#         },
#         "rocha-bruno": {
#             "slug": "rocha-bruno",
#             "titulo": "Coisas que NÃO devemos fazer ao programar em PYTHON - Codeshow",
#             "video_id": "p4jWEC7vuKI",
#         },
#     },
# )
# def test_titulo_video(resp, titulo):
#     assert_contains(resp, titulo)
