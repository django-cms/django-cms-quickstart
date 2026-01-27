from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include


def root_redirect(request):
    return redirect(f"/{settings.LANGUAGE_CODE}/")


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('taggit/', include('taggit_autosuggest.urls')),
    path('', root_redirect),
]

if settings.DEBUG:
    urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('cms.urls')),
)

# the new django admin sidebar is bad UX in django CMS custom admin views.
admin.site.enable_nav_sidebar = False
