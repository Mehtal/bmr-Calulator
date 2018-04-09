from django.db import models

# Create your models here.

class bmrcalc(models.Model):
	gender_choices = (
		('m' , "Male"),
		('f', 'Female')
		)
	age    = models.IntegerField()
	height = models.IntegerField()
	weight = models.IntegerField()
	gender = models.CharField(max_length=1 , choices=gender_choices,)
