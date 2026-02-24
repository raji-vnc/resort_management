from django.contrib import admin
from .models import Dashboard

admin.site.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
