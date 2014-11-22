from django.db import models
from countries_a.models import Country

# Create your models here.
class State(models.Model):
	state_name = models.CharField(max_length=255)
	country = models.ForeignKey(Country)

	def __unicode__(self):
		return self.state_name