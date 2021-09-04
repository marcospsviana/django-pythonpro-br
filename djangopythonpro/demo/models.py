from django.db import models


class Videos(models.Model):
    slug = models.CharField(max_length=35)
    titulo = models.CharField(max_length=60)
    video_id = models.CharField(max_length=35)
    created_at = models.DateTimeField(auto_now_add=True)
