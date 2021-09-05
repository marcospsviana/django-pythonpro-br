from django.db import models


class Autores(models.Model):
    titulo = models.CharField(max_length=60)

    def __str__(self):
        return self.titulo
