from django.contrib import admin
from .models import SondepompStatus

class SondepompStatusAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'status', 'timestamp', 'status_type', 'is_acknowledged')
    list_filter = ('status', 'status_type', 'device_id', 'is_acknowledged')
    search_fields = ('device_id', 'message')
    ordering = ('-timestamp',)
    readonly_fields = ('timestamp',)
    
    fieldsets = (
        ('Status Informatie', {
            'fields': ('status', 'status_type', 'is_acknowledged')
        }),
        ('Apparaat Details', {
            'fields': ('device_id', 'message')
        }),
        ('Tijdsinformatie', {
            'fields': ('timestamp',)
        }),
    )

admin.site.register(SondepompStatus, SondepompStatusAdmin)
