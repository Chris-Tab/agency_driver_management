from django.contrib import admin
from .models import ShiftRequest

@admin.register(ShiftRequest)
class ShiftRequestAdmin(admin.ModelAdmin):
    list_display = ('company', 'start_datetime', 'bonus', 'created_at')
    list_filter = ('company',)
    search_fields = ('company__username',)