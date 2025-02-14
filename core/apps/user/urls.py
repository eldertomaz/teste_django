from django.urls import path
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from core.apps.user import views


app_name = 'user'
router = DefaultRouter(trailing_slash=True)

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

router.register(r'technologies', views.TechnologiesViewSet, basename='technology')
router.register(r'programmers', views.ProgrammersViewSet, basename='programmer')
router.register(r'projects', views.ProjectsViewSet, basename='project')
router.register(r'allocations', views.AllocationsViewSet, basename='allocation')

urlpatterns = [
    #gerenciamento de user login
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterUserAPIView.as_view(), name='register'),

]+ router.urls