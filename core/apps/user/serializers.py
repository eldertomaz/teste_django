from rest_framework import serializers
from core.apps.user import models


class ProgrammersSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.Programmers
        fields = '__all__'