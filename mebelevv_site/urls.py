from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from mebelevv_site import settings

admin.site.site_header = 'MEBELEVV | Панель администратора'
admin.site.index_title = 'Таблицы'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mebelevv.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
