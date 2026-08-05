from django.contrib import admin
from .models import Waitlist


@admin.register(Waitlist)
class WaitlistAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "joined_at",
        "is_verified",
    )

    search_fields = ("email",)

    list_filter = (
        "is_verified",
        "joined_at",
    )