from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.apps.base.views import TenantBaseView
from core.apps.user import models
from core.apps.user import serializers

class RegisterUserAPIView(APIView):
    permission_classes = [AllowAny] 

    def post(self, request, *args, **kwargs):
        """
        Criar user.
        """

        data = request.data
        username = data.get('username')
        password = data.get('password')

        
        if not username or not password:
            return Response(
                {"error": "Username e/ou password vazios."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "User não permitido."},
                status=status.HTTP_400_BAD_REQUEST,
            )


        user = User.objects.create_user(username=username, password=password)
        return Response(
            {"message": "User criado.", "data":{"user_id": user.id}},
            status=status.HTTP_201_CREATED,
        )



class ProgrammersViewSet(TenantBaseView):

    serializer_class = serializers.ProgrammersSerializer
    queryset= models.Programmers.objects.all()
    
    # def get_queryset(self):
    #     """
    #     Retorna apenas os objetos do user logado.
    #     """
    #     return models.Programmers.objects.filter(tenant=self.request.user)
    
    # def perform_create(self, serializer):
    #     """
    #     Define o Tenant para o user logado.
    #     """
    #     serializer.save(tenant=self.request.user)
