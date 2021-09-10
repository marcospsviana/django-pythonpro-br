from decouple import config
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

# def trigger_error(request):
#     division_by_zero = 1 / 0


# def trigger_error(request):
#     division_by_zero = 1 / 0


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("djangopythonpro.base.urls")),
    path("demonstrativo/", include("djangopythonpro.demo.urls")),
    # path("sentry-debug/", trigger_error),
    path(
        "autores/",
        include("djangopythonpro.autores.urls"),
    ),
]

DEBUG = config("DEBUG", default=False, cast=bool)
if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(
        path("__debug__/", include(debug_toolbar.urls)),
    )
