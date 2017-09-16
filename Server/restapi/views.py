# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Farmer,Landlord
from django.core import serializers
# Create your views here.
def index(request):
	return HttpResponse('<h2> Welcome to rest server</h2>')

def farmerdetail(request):
	if request.method == 'POST':
		username = request.POST.get('username', None)
		data = { 'farmer_detail': serializers.serialize('json', Farmer.objects.all()) }
		res = JsonResponse(data)
		res['Access-Control-Allow-Origin']="*"
		print(res)
		return res

def landlorddetail(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        data = {'landlord_detail': serializers.serialize('json', Landlord.objects.all())}
        res = JsonResponse(data)
        res['Access-Control-Allow-Origin'] = "*"
        print(res)
        return res