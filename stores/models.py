from contacts.models import Contact
from django.db import models
from tabulators.models import Tabulator
from status_types.models import Status_Type
from addresses.models import Address
from django.contrib.auth.models import User 



# Create your models here.
class Store(models.Model):
	store_name = models.CharField(max_length=255)
	activity = models.CharField(max_length=255)
	dimentions_width = models.FloatField()
	dimentions_length = models.FloatField()
	address = models.ForeignKey(Address)



	store_phone = models.CharField(max_length=12)
	image1 = models.ImageField(upload_to='stores')
	image2 = models.ImageField(upload_to='stores', blank=True)
	image3 = models.ImageField(upload_to='stores', blank=True)
	image4 = models.ImageField(upload_to='stores', blank=True)
	image5 = models.ImageField(upload_to='stores', blank=True)
	website = models.CharField(max_length=255, blank=True)
	facebook = models.CharField(max_length=255, blank=True)
	twitter = models.CharField(max_length=255, blank=True)
	youtube = models.CharField(max_length=255, blank=True)
	comments = models.TextField(blank=True)
	contact = models.ForeignKey(Contact)
	tabulator = models.ForeignKey(Tabulator)
	status = models.ForeignKey(Status_Type)
	date_created = models.DateField(null=True, blank=True)
	date_approved = models.DateField(null=True, blank=True)
	username = models.ForeignKey(User)


	wireless = models.BooleanField(default=False)
	stands = models.BooleanField(default=False)
	repisas = models.BooleanField(default=False)
	boards = models.BooleanField(default=False)
	lighting = models.BooleanField(default=False)
	electricity = models.BooleanField(default=False)
	water = models.BooleanField(default=False)
	airconditioning = models.BooleanField(default=False)
	toilets = models.BooleanField(default=False)
	heating = models.BooleanField(default=False)
	elevator = models.BooleanField(default=False)
	parkinglot = models.BooleanField(default=False)
	counter = models.BooleanField(default=False)
	phoneline = models.BooleanField(default=False)
	storehouse = models.BooleanField(default=False)
	dressingroom = models.BooleanField(default=False)
	others1 = models.BooleanField(default=False)
	others2 = models.BooleanField(default=False)
	others3 = models.BooleanField(default=False)

	#Ojo: Faltan los campos para los lugares cercanos
	
	price = models.FloatField(blank=True)

	def __unicode__(self):
		return self.store_name

	def Precio_por_Dia(self):
		return self.tabulator.suggested_price

	def Precio_por_Semana(self):
		precio_semana = (self.tabulator.suggested_price * 6)*.95
		return precio_semana

	def Precio_por_Mes(self):
		precio_mes = (self.tabulator.suggested_price * 30)*.90
		return precio_mes

	def Tienda(self):
		return self.store_name

	def Contacto(self):
		return self.contact

	def Telefono(self):
		return self.store_phone

	def Correo(self):
		return self.contact.email

	def Direccion(self):
		return """
				<p>%s,</p>
				<p>%s,</p>
				<p>%s,</p>
				<p>%s,</p>
				<p>%s,</p>
				""" % (self.address, self.address.neighborhood, self.address.postal_code, self.address.postal_code.town, self.address.postal_code.town.city)

	def Verificacion(self):
		return self.status

	#Falta hacer la funcion para calcular el num. de solicitudes
	def Solicitudes(self):
		return '5'

	def EditaStatus(self):
		return self.status.status_name

	Direccion.allow_tags = True
	Direccion.admin_order_field = 'address'
	Tienda.admin_order_field = 'store_name'
	Contacto.admin_order_field = 'contact'
	Verificacion.admin_order_field = 'status'
	#Falta ordenar por solicitudes

	




