from django.db import models

# Create your models here.

class Vehicle(models.Model):
    plate = models.CharField(max_length=200)

class NavigationRecord(models.Model):
	date_time = models.DateTimeField()
	vehicle = models.ForeignKey(
	    Vehicle,
	    on_delete=models.CASCADE,
	)
	latitude = 	models.FloatField()
	longitude = models.FloatField()
