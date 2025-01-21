from django.contrib import admin
from .models import Flat
from .models import Complaint


class FlatAdmin(admin.ModelAdmin):
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town', 'owner_pure_phone']
    list_editable = ['new_building']

    readonly_fields = ['created_at']

    search_fields = ['town', 'address', 'owner']

    list_filter = ['new_building', 'rooms_number', 'construction_year', 'town', 'has_balcony']

    raw_id_fields = ['liked_by']


admin.site.register(Flat, FlatAdmin)


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['user', 'flat', 'created_at']

    list_filter = ['created_at']

    raw_id_fields = ['user', 'flat']


admin.site.register(Complaint, ComplaintAdmin)