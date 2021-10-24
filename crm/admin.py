from django.contrib import admin
from . import models

#admin.site.register(models.Client)
admin.site.register(models.Call)
admin.site.register(models.Deal)
admin.site.register(models.Reminder)

@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'lpr', 'tel_number', 'adress')
    list_filter = ('client_name', 'adress')
    search_fields = ('client_name', 'commentary')
    ordering = ('client_name', 'adress')

