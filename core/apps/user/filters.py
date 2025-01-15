import django_filters

from core.apps.base.filters import BaseFilter
from .models import Technologies, Programmers, Projects, Allocations

class TechnologiesFilter(BaseFilter, django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Technologies
        fields = ['name']


class ProgrammersFilter(BaseFilter, django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    technologies = django_filters.ModelMultipleChoiceFilter(
        queryset=Technologies.objects.all(),
        conjoined=True  
    )

    class Meta:
        model = Programmers
        fields = ['name', 'technologies']


class ProjectsFilter(BaseFilter, django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    start_date = django_filters.DateFilter(field_name='start_date', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='end_date', lookup_expr='lte')
    technologies = django_filters.ModelMultipleChoiceFilter(
        queryset=Technologies.objects.all(),
        conjoined=False  
    )

    class Meta:
        model = Projects
        fields = ['name', 'start_date', 'end_date', 'technologies']


class AllocationsFilter(BaseFilter, django_filters.FilterSet):
    project = django_filters.ModelChoiceFilter(queryset=Projects.objects.all())
    programmer = django_filters.ModelChoiceFilter(queryset=Programmers.objects.all())
    hours = django_filters.NumberFilter(lookup_expr='gte')

    class Meta:
        model = Allocations
        fields = ['project', 'programmer', 'hours']
