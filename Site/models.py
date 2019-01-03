# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.db import models

# Create your models here.
class Page(models.Model):
    type = models.CharField(max_length=10, unique=True, verbose_name='Typ strony')
    title = models.CharField(max_length=100, verbose_name='Tytuł')
    #image = models.ImageField(height_field=250, width_field=500)
    extras = models.TextField(null=True)
    content = models.TextField(verbose_name='Treść')
    last_edit = models.DateTimeField(auto_now=True, verbose_name='Data ostatniej edycji')

    class Meta:
        verbose_name = 'Podstrona'
        verbose_name_plural = 'Podstrony'

    def __str__(self):
        return self.title

    def get_extras(self):
        return json.loads(self.extras)