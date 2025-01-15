from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend


from core.apps.base.views import TenantBaseView
from core.apps.user import models
from core.apps.user import serializers
from core.apps.user import filters


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


class GenericViewSet(TenantBaseView):
    serializers = serializers

    def get_filterset_kwargs(self):
        kwargs = super().get_filterset_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class TechnologiesViewSet(GenericViewSet):
    model = models.Technologies
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.TechnologiesFilter

class ProgrammersViewSet(GenericViewSet):
    model = models.Programmers
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.ProgrammersFilter

class ProjectsViewSet(GenericViewSet):
    model = models.Projects
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.ProjectsFilter


class AllocationsViewSet(GenericViewSet):
    model = models.Allocations
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.AllocationsFilter
