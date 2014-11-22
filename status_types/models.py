from django.db import models

# Create your models here.
class Status_Type(models.Model):
	status_name = models.CharField(max_length=11)

	def __unicode__(self):
		return self.status_name