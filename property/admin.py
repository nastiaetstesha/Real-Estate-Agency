from django.contrib import admin
from .models import Flat, Complaint, Owner


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['user', 'flat', 'created_at']
    list_filter = ['created_at']
    raw_id_fields = ['user', 'flat']

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ["full_name", "phone_number", "pure_phone_number"]
    search_fields = ["full_name", "phone_number", "pure_phone_number"]
    raw_id_fields = ["flats"]


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ['owner', 'flat']
    extra = 1

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town']
    list_editable = ['new_building']
    readonly_fields = ['created_at']
    search_fields = ['town', 'address']
    list_filter = ['new_building', 'rooms_number', 'construction_year', 'town', 'has_balcony']
    raw_id_fields = ['liked_by']
    inlines = [OwnerInline]
