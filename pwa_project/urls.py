from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from django.conf.urls.static import static
from django.conf import settings
from . import views
handler404 = 'pwa_project.views.handler404'
handler500 = 'pwa_project.views.handler500'
urlpatterns = [
    path('', include('exemple.urls')),
    path('admin/', admin.site.urls),
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
