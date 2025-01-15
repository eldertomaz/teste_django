
from django.contrib import admin
from django.urls import path,include
from .swagger import schema_view

urlpatterns = [
    path('user/', include('core.apps.user.urls', namespace='user')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),

    #path('admin/', admin.site.urls),
]
