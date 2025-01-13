from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from django.contrib import admin


app_name = 'programmer'
router = DefaultRouter(trailing_slash=True)

urlpatterns = [
    path('admin/', admin.site.urls),
]
