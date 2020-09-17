from django.shortcuts import render
from q2.models import *
# Create your views here.

def q2_fill():
	f = open("input_q2.txt", "r")
	line = f.readline()
	line = f.readline()
	while line != "Operations\n":
		obj_list = line.split(",")
		b = Bin(latitude=obj_list[0],longitude=obj_list[1])
		b.save()
		line = f.readline()
	line = f.readline()

	while line != "Usage\n":
		line = line.strip("\n")
		o = Operation(name=line)
		o.save()
		line = f.readline()

	line = f.readline()		
	while line != "":	
		obj_list = line.split(",")
		b = Bin.objects.get(pk=int(obj_list[0]))
		o = Operation.objects.get(name=obj_list[1])
		u = Use(id_bin=b,id_op=o,last_collection=obj_list[2],collection_frequency=obj_list[3])
		u.save()
		line = f.readline()

def q2_retrieve():
	use_list = Use.objects.values("id_bin_id","id_op__name","collection_frequency")
	return list(use_list)