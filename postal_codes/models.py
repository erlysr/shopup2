from django.db import models
from towns.models import Town


# Create your models here.
class Postal_Code(models.Model):
	postal_code_key = models.CharField(max_length=5)
	town = models.ForeignKey(Town)

	def __unicode__(self):
		return self.postal_code_key