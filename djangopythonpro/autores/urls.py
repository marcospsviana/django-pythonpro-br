from django.urls import path

from djangopythonpro.autores import views

app_name = "autores"

urlpatterns = [
    path("<slug>", views.detalhes, name="detalhes"),
]
