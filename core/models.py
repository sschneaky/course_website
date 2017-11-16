from django.db import models

# Create your models here.

class ClassPeriod(models.Model):
	
		date = models.DateField()

		slide = models.CharField(max_length=100, null=True, blank=True)
		slide_url = models.CharField(max_length=100, null=True, blank=True)

		reading = models.CharField(max_length=100, null=True, blank=True)
		reading_url = models.CharField(max_length=100, null=True, blank=True)

		events = models.CharField(max_length=100, null=True, blank=True)
		events_url = models.CharField(max_length=100, null=True, blank=True)
