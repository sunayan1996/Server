# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Farmer,Landlord
# Register your models here.

admin.site.register(Farmer)
admin.site.register(Landlord)