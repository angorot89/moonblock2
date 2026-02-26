from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "MOONBLOCK Admin"
admin.site.site_title = "Moonblock"
admin.site.index_title = "Store Management"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
