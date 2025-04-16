from django.contrib import admin

from .models import Flat, Complaint

class FlatAdmin(admin.ModelAdmin):
    list_display = (
        'address', 'owners_phonenumber', 'owner_pure_phone',
        'price','new_building', 'construction_year', 'town'
    )
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    search_fields = ('town','address', 'owner')
    readonly_fields = ["created_at"]
    pass

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', 'user')
    list_display = (
        'flat', 'user', 'complaint_text',
        )

admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)