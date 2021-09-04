from django.contrib.admin import ModelAdmin, register
from .models import Videos


@register(Videos)
class VideoAdmin(ModelAdmin):
    list_display = ["slug", "titulo", "video_id", "created_at"]
    prepopulated_fields = {"slug": ("titulo",)}
