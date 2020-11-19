from django.contrib import admin
from pheeds import models as pheed_models


@admin.register(pheed_models.Pheed)
class PheedAdmin(admin.ModelAdmin):

    """ Pheed Admin Definition """

    list_display = (
        "__str__",
        "likes",
    )