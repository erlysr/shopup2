from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
	list_display = ('firstname', 'lastname', 'contact_phone', 'email')

# Register your models here.
admin.site.register(Contact, ContactAdmin)