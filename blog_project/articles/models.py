# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ArticlesV1(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=True)
    author = models.CharField(max_length=20)
    body = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']
