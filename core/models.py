from django.db import models

# Create your models here.

class ClassPeriod(models.Model):
	
	date = models.DateField(primary_key=True, unique=True)

	title = models.CharField(max_length=100, null=True, blank=True)
	url = models.CharField(max_length=200, null=True, blank=True)

	class Meta:
		ordering = ['date']

	def __str__(self):
		return f'{self.date} : {self.title}'



class Reading(models.Model):

	class_period = models.ForeignKey(ClassPeriod. on_delete=models.PROTECT)
	title = title = models.CharField(max_length=100, null=True, blank=True)
	url = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return f'{self.title}'
		


class Event(models.Model):
	class_period = models.ForeignKey(ClassPeriod, on_delete=models.PROTECT)
	title = models.CharField(max_length=100, null=True, blank=True)
	url = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return f'{self.title}'