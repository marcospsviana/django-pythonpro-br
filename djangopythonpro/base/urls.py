from django.urls import path, include

from djangopythonpro.base.views import home


app_name = "base"
urlpatterns = [
    path("", home, name="home"),
    path("demonstrativo/", include('djangopythonpro.demo.urls')),
]
