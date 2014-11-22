from django.db import models
from cities.models import City


# Create your models here.
class Town(models.Model):
	town_name = models.CharField(max_length=255)
	city = models.ForeignKey(City)

	def __unicode__(self):
		return self.town_name
