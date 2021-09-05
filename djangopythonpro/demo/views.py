from django.shortcuts import render, get_object_or_404
from djangopythonpro.demo.models import Videos


def indice(request):
    video = Videos.objects.order_by("created_at").all()
    return render(request, "demonstrativo/indice.html", context={"video": video})


def video(request, slug):
    video_data = get_object_or_404(Videos, slug=slug)
    return render(request, "demonstrativo/video.html", context={"video": video_data})
