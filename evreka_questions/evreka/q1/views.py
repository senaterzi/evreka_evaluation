from django.shortcuts import render
from q1.models import *
from django.db.models import Max 
from datetime import datetime, timedelta
from django.utils import timezone
import pytz
# Create your views here.


def q1_fill():
	f = open("input_q1.txt", "r")
	line = f.readline()
	line = f.readline()
	while line != "NavigationRecords\n":
		line = line.rstrip("\n")
		v = Vehicle(plate=line)
		v.save()
		line = f.readline()
	line = f.readline()

	while line != "":	
		obj_list = line.split(",")
		print(obj_list[0])
		v = Vehicle.objects.get(plate=obj_list[0])
		
		n = NavigationRecord(date_time=obj_list[1],vehicle=v,latitude=obj_list[2],longitude=obj_list[2]) 
		n.save()
		line = f.readline()

def q1_retrieve():
	thetime = timezone.now() - timedelta(hours=48)
	l = NavigationRecord.objects.values('vehicle').filter(date_time__gte=thetime).annotate(Max('date_time')) 
	last_points = []
	for plate in l:
		record = NavigationRecord.objects.values('vehicle__plate','date_time','latitude','longitude').filter(date_time=plate['date_time__max'],vehicle=plate['vehicle'])
		record_list = list(record)[0]
		record_list["date_time"] = record_list["date_time"].strftime("%d.%m.%Y %H:%M:%S") 		
		last_points.append(record_list)
	return last_points	