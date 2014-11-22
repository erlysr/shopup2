from django.db import models
from stores.models import Store
from towns.models import Town

# Create your models here.
class Byzone_Topup(models.Model):
	zone_name = models.CharField(max_length=255)
	store = models.ManyToManyField('stores.Store')
	town = models.ForeignKey(Town)
	priority = models.PositiveIntegerField()

	def __unicode__(self):
		return self.zone_name
