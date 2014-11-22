from django.contrib import admin
from .models import Store
from store_requests.models import Store_Request
from tabulators.models import Tabulator
 

class Store_RequestInLine(admin.StackedInline):
	model = Store_Request
	extra = 0


class StoreAdmin(admin.ModelAdmin):
	#Checar como cambiar las etiquetas a espanol para que acepte acentos
	list_display = ('Tienda', 'Contacto', 'Telefono', 'Correo', 'Direccion', 'status', 'Solicitudes', 'Precio_por_Dia', 'Precio_por_Semana', 'Precio_por_Mes')
	ordering = ('-status', 'store_name')
	list_filter = ('store_name', 'status')
	search_fields = ('store_name', 'contact__firstname', 'address__address_line1', 'address__neighborhood')
	list_editable = ('status', )
	inlines = [Store_RequestInLine, ]
	change_list_template = "admin/change_list_filter_sidebar.html"

# Register your models here.
admin.site.register(Store, StoreAdmin)