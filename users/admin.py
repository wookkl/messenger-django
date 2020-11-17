from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from users import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "bio",
                    "avatar",
                    "status_message",
                )
            },
        ),
    )

    list_display = (
        "username",
        "email",
        "status_message",
        "get_friends_count",
        "is_superuser",
        "is_staff",
    )

    list_filter = (
        "is_superuser",
        "is_staff",
    )