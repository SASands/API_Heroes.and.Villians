from operator import mod
from tkinter import CASCADE
from django.db import models

import super_types

# Create your models here.

class Super(models.Model):
    name = models.CharField(max_length=100)
    alter_ego = models.CharField(max_length=100)
    primary_ability = models.CharField(max_length=255)
    secondary_ability = models.CharField(max_length=255)
    catchphrase = models.CharField(max_length=255)
    super_type = models.ForeignKey(Super, on_delete=CASCADE )

