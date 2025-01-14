from rest_framework import serializers
from django.db.models import Sum

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

    def validate(self, data):
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        #Horas planejadas para o projeto 
        # só podem ser distribuídas dentro 
        # do intervalo definido por Data Inicial e Data Final.
        if start_date and end_date and start_date > end_date:
            raise serializers.ValidationError(
                "A data de início não pode ser maior que a data de finalização."
            )

        return data



class AllocationsSerializer(BaseSerializer):

    class Meta:

        model = models.Allocations
        fields = '__all__'

    def validate(self, data):

        tenant = self.context['request'].user

        programmer = data['programmer']
        project = data['project']
        hours = data['hours']

        # Um desenvolvedor só pode ser alocado em um projeto 
        # se ele possuir pelo menos uma tecnologia que o projeto exige.
        project_technologies = set(project.technologies.filter(tenant=tenant))
        programmer_technologies = set(programmer.technologies.filter(tenant=tenant))
        if not project_technologies.intersection(programmer_technologies):
            raise serializers.ValidationError(
                "O desenvolvedor deve possuir pelo menos uma tecnologia exigida pelo projeto."
            )


        # O total de horas alocadas para todos os desenvolvedores 
        # em um projeto não pode ultrapassar as horas planejadas para o projeto.
        total_days = (project.end_date - project.start_date).days + 1
        total_allocated_hours = (
            project.allocations_projects.aggregate(total=Sum('hours'))['total'] or 0
        )
        if total_allocated_hours + hours > (project.hours_day * total_days):
            raise serializers.ValidationError(
                "O total de horas alocadas não pode ultrapassar as horas planejadas para o projeto."
            )

        return data