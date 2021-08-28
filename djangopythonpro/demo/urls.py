from django.urls import path

from djangopythonpro.demo.views import video

app_name = "demo"
urlpatterns = [
    path("<slug:slug>", video, name="video"),
]
