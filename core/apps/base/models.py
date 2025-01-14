from django.db import models
from django.contrib.auth.models import User



class BaseModel(models.Model):

    tenant = models.ForeignKey(User,
        on_delete=models.CASCADE,
        related_name="%(class)s_tenant", 
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True  

