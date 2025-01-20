from django.contrib import admin
from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at']

    search_fields = ['town', 'address', 'owner']


admin.site.register(Flat, FlatAdmin)
