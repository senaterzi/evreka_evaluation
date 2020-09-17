from django.db import models

# Create your models here.
class Bin(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

class Operation(models.Model):
    name = models.CharField(max_length=200)

class Use(models.Model):
	id_bin = models.ForeignKey(
	    Bin,
	    on_delete=models.CASCADE,
	)
	id_op = models.ForeignKey(
	    Operation,
	    on_delete=models.CASCADE,
	)
	collection_frequency = 	models.IntegerField()
	last_collection = models.DateTimeField()

