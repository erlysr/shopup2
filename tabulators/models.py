from django.db import models
from towns.models import Town

# Create your models here.
class Tabulator(models.Model):
	tab_zone = models.CharField(max_length=255)
	town = models.ForeignKey(Town)
	min_price = models.IntegerField()
	max_price = models.IntegerField()
	media_price = models.IntegerField()
	suggested_price = models.IntegerField(blank=True)


	def __unicode__(self):
		return self.tab_zone

	def Delegacion(self):
		return self.town.town_name

	def Precio_Minimo(self):
		return self.min_price

	def Precio_Maximo(self):
		return self.max_price

	def Media_Precio(self):
		return self.media_price

	def Estado(self):
		return self.town.city.state

