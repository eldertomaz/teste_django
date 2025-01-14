from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class TenantBaseView(viewsets.ModelViewSet):
    """
    1: tenant é definido como o user logado.
    2: Apenas os objetos do tenant são acessados.
    """
    permission_classes = [IsAuthenticated]  
    
    def get_serializer_class(self):
        """
        padrao: <ModelName>Serializer.
        """
        serializer_class = getattr(self, 'serializer_class', None)
        if serializer_class:
            return serializer_class
        else:
            return getattr(self.serializers, self.model.__name__ + 'Serializer')
    
    def get_queryset(self):

        queryset = self.model.objects.get_queryset()
        return queryset.filter(tenant=self.request.user)

    def perform_create(self, serializer):

        serializer.save(tenant=self.request.user)
