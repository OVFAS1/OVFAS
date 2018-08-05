from django.db import models
from django.contrib.admin.widgets import AdminDateWidget
from django.core.validators import RegexValidator
import os
from django.contrib.auth.models import Permission,User

class HostelBlock(models.Model):
    block_name=models.CharField(max_length=100)

    def __str__(self):
        return(self.block_name)


