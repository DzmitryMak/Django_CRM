from django.contrib import admin
from . import models

#admin.site.register(models.Client)
admin.site.register(models.Call)
admin.site.register(models.Deal)
admin.site.register(models.Reminder)

@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('company', 'contact_name', 'phone', 'address')
    list_filter = ('company', 'address')
    search_fields = ('company', 'commentary')
    ordering = ('company', 'address')

