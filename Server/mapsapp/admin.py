# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis import admin
from .models import Farms, Household, Well
# Register your models here.
admin.site.register(Farms, admin.OSMGeoAdmin)
admin.site.register(Household, admin.OSMGeoAdmin)
admin.site.register(Well, admin.OSMGeoAdmin)