from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from app.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
