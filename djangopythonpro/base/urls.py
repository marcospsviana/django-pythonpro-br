from django.urls import path

from djangopythonpro.base.views import home
from djangopythonpro.demo.views import video

app_name = "base"
urlpatterns = [
    path("", home, name="home"),
    path("demonstrativo/", video, name="video"),
]
