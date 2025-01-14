from rest_framework import serializers

from core.apps.base.serializers import BaseSerializer
from core.apps.user import models


class TechnologiesSerializer(BaseSerializer):

    class Meta:

        model = models.Technologies
        fields = '__all__'


class ProgrammersSerializer(BaseSerializer):

    class Meta:

        model = models.Programmers
        fields = '__all__'


class ProjectsSerializer(BaseSerializer):

    class Meta:

        model = models.Projects
        fields = '__all__'


class AllocationsSerializer(BaseSerializer):

    class Meta:

        model = models.Allocations
        fields = '__all__'