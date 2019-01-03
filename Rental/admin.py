# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Car)
admin.site.register(User)
admin.site.register(District)
admin.site.register(City)
admin.site.register(CityType)