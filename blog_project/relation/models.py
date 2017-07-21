# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Api(models.Model):
    api_id = models.CharField(max_length=100)
    api_functions = models.CharField(max_length=100)
    sour_s = models.CharField(max_length=30)
    dest_s = models.CharField(max_length=30)
