from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API para alocação de desenvolvedores",
        default_version='v1',
        description="Documentação interativa da API para teste da Verzel",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="eldertomazinho@gmail.com"),
        license=openapi.License(name="MIT License"),
        #x_logo={"url": "https://verzel.com.br/landings/assets/images/logo_icon_verzel_white.svg"}
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    #urlconf='core.urls'
)
