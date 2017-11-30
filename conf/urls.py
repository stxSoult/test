
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^utils/', include('app.utils.urls', namespace='utils')),

    url(r'^', include('app.posts.urls', namespace='posts')),
    url(r'^', include('app.accounts.urls', namespace='accounts'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



