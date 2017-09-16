# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Farmer(models.Model):
	name = models.CharField(max_length=250)
	dob = models.DateField(max_length=250)
	address = models.CharField(max_length=550)
	mobile_no = models.CharField(max_length=250)
	password = models.CharField(max_length=250)

class Landlord(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=550)
    mobile_no = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    acerage = models.FloatField()