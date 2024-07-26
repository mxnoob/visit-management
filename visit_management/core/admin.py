from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import Shop, Visit, Worker


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("phone_number", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("phone_number", "password1", "password2"),
            },
        ),
    )
    list_display = ("id", "name", "phone_number")
    list_filter = ("phone_number",)
    ordering = ("phone_number",)
    search_fields = ["name"]


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    search_fields = ["name"]


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    search_fields = ["worker__name", "shop__name"]
