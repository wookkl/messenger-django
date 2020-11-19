from django.contrib import admin
from friends import models as friend_models


@admin.register(friend_models.Friend)
class FriendAdmin(admin.ModelAdmin):

    """ Friend Admin Definition """

    list_display = ("__str__",)
    filter_horizontal = ("friend",)
