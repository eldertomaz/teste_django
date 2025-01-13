
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('register/', include('core.apps.user.urls', namespace='register')),
    path('programmer/', include('core.apps.programmer.urls', namespace='programmer')),

    path('admin/', admin.site.urls),
]
