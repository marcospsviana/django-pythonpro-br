from ordered_model.models import OrderedModel
from django.db import models


class Autores(OrderedModel):
    titulo = models.CharField(max_length=60)
    descricao = models.TextField()
    slug = models.SlugField(unique=True)

    class Meta(OrderedModel.Meta):
        pass

    def get_absolute_url(self):
        return f'autores/{self.slug}'

    def __str__(self):
        return self.titulo
