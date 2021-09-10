from ordered_model.models import OrderedModel
from django.db import models
from django.shortcuts import reverse



class Autores(OrderedModel):
    titulo = models.CharField(max_length=60)
    descricao = models.TextField()
    slug = models.SlugField(unique=True)

    class Meta(OrderedModel.Meta):
        pass

    def get_absolute_url(self):
        return reverse("autores:detalhes", kwargs={"slug": self.slug})


    def __str__(self):
        return self.titulo
