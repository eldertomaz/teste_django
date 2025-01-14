from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User

from core.apps.base.models import BaseModel

# class Technologies




class Programmers(BaseModel):

    full_name = models.CharField( max_length=200)
