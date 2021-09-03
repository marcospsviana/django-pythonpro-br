from django.shortcuts import render
from djangopythonpro.demo.models import Videos


# videos_class = [
#     Videos("renzo", "os fodásticos do python dev pro", "a61p-g0yWts"),
#     Videos(
#         "rocha-bruno",
#         "Coisas que NÃO devemos fazer ao programar em PYTHON - Codeshow",
#         "p4jWEC7vuKI",
#     ),
# ]
videos_class = [
    {
        "slug": "renzo",
        "titulo": "os fodásticos do python dev pro",
        "video_id": "a61p-g0yWts",
    },
    {
        "slug": "rocha-bruno",
        "titulo": "Coisas que NÃO devemos fazer ao programar em PYTHON - Codeshow",
        "video_id": "p4jWEC7vuKI",
    },
]

videos_slugs = {vid["slug"]: vid for vid in videos_class}


def indice(request):
    return render(request, "demonstrativo/indice.html", context={"video": videos_class})


def video(request, slug):
    video_data = Videos.objects.filter(slug=slug)
    print(f'video_data {video_data}')
    return render(request, "demonstrativo/video.html", context={"video": video_data})
