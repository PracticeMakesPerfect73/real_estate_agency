from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flat.through
    extra = 0
    raw_id_fields = ('owner', 'flat')
    verbose_name = 'Владелец'
    verbose_name_plural = 'Владельцы'


class FlatAdmin(admin.ModelAdmin):
    list_display = (
        'address', 'price', 'new_building',
        'construction_year', 'town'
    )
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    search_fields = ('town', 'address')
    readonly_fields = ["created_at"]
    inlines = [OwnerInline]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', 'user')
    list_display = (
        'flat', 'user', 'complaint_text',
        )


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)
    list_display = ('owner', 'pure_phonenumber')
    search_fields = ('owner', 'pure_phonenumber')


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
