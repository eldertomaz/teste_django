from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class TenantBaseView(viewsets.ModelViewSet):
    """
    1. tenant é definido como o user logado.
    2. Apenas os objetos do tenant são acessados.
    """
    permission_classes = [IsAuthenticated]  
    def get_queryset(self):

        queryset = super().get_queryset()
        return queryset.filter(tenant=self.request.user)

    def perform_create(self, serializer):

        serializer.save(tenant=self.request.user)
