from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Videos(models.Model):
    titulo = models.CharField(max_length=60)
    slug = models.SlugField(max_length=35)
    video_id = models.CharField(max_length=35)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("demo:video", args=(self.slug,))

    def __str__(self):
        return f"Vídeo: {self.slug}"

    class Meta:
        verbose_name_plural = _("videos")
