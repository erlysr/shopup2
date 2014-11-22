from django.db import models

# Create your models here.
class Contact(models.Model):
	firstname = models.CharField(max_length=255)
	lastname = models.CharField(max_length=255)
	contact_phone = models.CharField(max_length=12)
	email = models.CharField(max_length=255)

	def __unicode__(self):
		return self.firstname
