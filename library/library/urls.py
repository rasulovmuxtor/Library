from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from ebooks.views import ApiRoot

urlpatterns = [
    path("",ApiRoot.as_view(),name="root-endpoints"),
    path('admin/', admin.site.urls),
    path('api/admin/',include('admin_api.urls')),
    path('user/',include('user.urls')),
    path('ebooks/',include('ebooks.urls')),
    path('books/',include('books.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)