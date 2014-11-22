from django.contrib import admin
from .models import Topup

class TopupsAdmin(admin.ModelAdmin):
	list_display = ('topup_name', 'Imagen')
# Register your models here.
admin.site.register(Topup, TopupsAdmin)