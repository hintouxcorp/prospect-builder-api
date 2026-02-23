from django.contrib import admin
from .models import House

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "type",
        "status",
        "phone",
        "whatsapp",
        "visits",
        "created_at",
    )

    list_filter = ("type", "status")

    search_fields = ("name", "email", "phone", "whatsapp")
