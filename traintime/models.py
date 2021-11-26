from django.db import models
from datetime import datetime

# Create your models here.
class Train(models.Model):
	slNo = models.IntegerField(max_length = 50)
	Date =  models.DateField(max_length = 50)
	TrainName = models.CharField(max_length = 50)
	DepartureFrom = models.CharField(max_length = 50)
	Departuretime =models.TimeField(max_length = 50)
	Departuretime =models.TimeField(max_length = 50)
	ArrivingAt = models.CharField(max_length = 50)
	Arrivaltime =models.TimeField(max_length = 50)
	class Meta:
			   db_table = "Train"
