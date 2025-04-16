from django.contrib import admin

from .models import Flat

class FlatAdmin(admin.ModelAdmin):
    list_display = (
        'address', 'price','new_building', 'construction_year', 'town'
    )
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    search_fields = ('town','address', 'owner')
    readonly_fields = ["created_at"]
    pass


admin.site.register(Flat, FlatAdmin)
