from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from core.apps.base.models import BaseModel


class Technologies(BaseModel):
    
    name = models.CharField( max_length=100)


class Programmers(BaseModel):

    name = models.CharField( max_length=100)
    technologies = models.ManyToManyField(Technologies, 
        related_name='programmers_technologies',
        blank=True,
        null=True,)


class Projects(BaseModel): 
    
    name = models.CharField(max_length=100) 
    start_date = models.DateField() 
    end_date = models.DateField() 
    hours_day = models.IntegerField(default=8,
        validators=[MinValueValidator(0), 
            MaxValueValidator(24)])
    
    technologies = models.ManyToManyField(Technologies, 
        related_name='projects_technologies')


class Allocations(BaseModel): 
    project = models.ForeignKey(Projects, 
        on_delete=models.CASCADE, 
        related_name='allocations_projects') 
    programmer = models.ForeignKey(Programmers, 
        on_delete=models.CASCADE, 
        related_name='allocations_programmers') 
    hours = models.IntegerField()