from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(path('__debug__', include(debug_toolbar.urls)))
