# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
import datetime

# Create your models here.
class Farms(models.Model):
    farm_id = models.AutoField(primary_key=True)
    farm_name = models.CharField(max_length=50)
    owner_name = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    farm_polygon = models.PolygonField(srid=4326,geography=True)
    area = models.FloatField(default=0.0)
    
#    def save(self):
#	temp=self.farm_polygon.transform(27700,clone=True)
#	self.area=temp.area
#	super(save,self).save(self)
    

class Household(models.Model):
    household_id = models.AutoField(primary_key=True)
    owner_name = models.CharField(max_length=50)
    income = models.IntegerField()
    location = models.PointField(null =True)
    no_of_members = models.IntegerField()


class Well(models.Model):
#    farm_id=models.ForeignKey(Farms,to_field='farm_id',on_delete=models.CASCADE)
    well_id = models.AutoField(primary_key=True)
    owner_name = models.CharField(max_length=50)
    location = models.PointField(null =True)
    depth = models.FloatField()
    average_yield = models.FloatField()
