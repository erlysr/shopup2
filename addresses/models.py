from django.db import models
from postal_codes.models import Postal_Code


# Create your models here.
class Address(models.Model):
	address_line1 = models.CharField(max_length=255)
	neighborhood = models.CharField(max_length=255)
	postal_code = models.ForeignKey(Postal_Code)
	
	def __unicode__(self):
		return self.address_line1