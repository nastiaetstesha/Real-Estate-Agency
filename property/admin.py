from django.contrib import admin
from .models import Flat
from .models import Complaint, Owner



class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['user', 'flat', 'created_at']

    list_filter = ['created_at']

    raw_id_fields = ['user', 'flat']


admin.site.register(Complaint, ComplaintAdmin)


class OwnerAdmin(admin.ModelAdmin):
    list_display = ["full_name", "phone_number", "pure_phone_number"]
    search_fields = ["full_name", "phone_number", "pure_phone_number"]
    raw_id_fields = ["flats"]


admin.site.register(Owner, OwnerAdmin)


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ['owner', 'flat']
    extra = 1


class FlatAdmin(admin.ModelAdmin):
    list_display = ['address', 'price', 'new_building', 'construction_year', 'town', 'owners_phonenumber', 'owner_pure_phone']
    list_editable = ['new_building']

    readonly_fields = ['created_at']
    readonly_fields = ['owner_pure_phone']

    search_fields = ['town', 'address', 'owner']

    list_filter = ['new_building', 'rooms_number', 'construction_year', 'town', 'has_balcony']

    raw_id_fields = ['liked_by']
    raw_id_fields = ['owners']
    inlines = [OwnerInline]

admin.site.register(Flat, FlatAdmin)
