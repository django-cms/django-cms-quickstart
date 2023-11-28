from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),  # Añade la URL para el seteo del idioma
]

urlpatterns += i18n_patterns(
    path('', include('cms.urls')),
    # Aquí puedes incluir otras rutas que quieras internacionalizar
    prefix_default_language=True # Añade esto si no quieres que el idioma por defecto tenga un prefijo en la URL
)

if settings.DEBUG:
    urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

# the new django admin sidebar is bad UX in django CMS custom admin views.
admin.site.enable_nav_sidebar = False