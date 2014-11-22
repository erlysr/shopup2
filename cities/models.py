from django.db import models
from states_a.models import State 


# Create your models here.
class City(models.Model):
	city_name = models.CharField(max_length=255)
	state = models.ForeignKey(State)

	def __unicode__(self):
		return self.city_name
