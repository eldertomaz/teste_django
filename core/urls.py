
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('user/', include('core.apps.user.urls', namespace='user')),
    

    path('admin/', admin.site.urls),
]
