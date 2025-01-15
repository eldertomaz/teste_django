import django_filters

from core.apps.base.filters import BaseFilter
from core.apps.user import models

class TechnologiesFilter(BaseFilter, django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.Technologies
        fields = ['name']


class ProgrammersFilter(BaseFilter, django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    technologies = django_filters.ModelMultipleChoiceFilter(
        queryset = models.Technologies.objects.all(),
        conjoined = True  
    )

    class Meta:
        model = models.Programmers
        fields = ['name', 'technologies']


class ProjectsFilter(BaseFilter, django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    start_date = django_filters.DateFilter(field_name='start_date', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='end_date', lookup_expr='lte')
    technologies = django_filters.ModelMultipleChoiceFilter(
        queryset = models.Technologies.objects.all(),
        conjoined=False  
    )

    class Meta:
        model = models.Projects
        fields = ['name', 'start_date', 'end_date', 'technologies']


class AllocationsFilter(BaseFilter, django_filters.FilterSet):
    project = django_filters.ModelChoiceFilter(queryset = models.Projects.objects.all())
    programmer = django_filters.ModelChoiceFilter(queryset = models.Programmers.objects.all())
    hours = django_filters.NumberFilter(lookup_expr='gte')

    class Meta:
        model = models.Allocations
        fields = ['project', 'programmer', 'hours']
