from django.contrib import admin
from conversations import models as conversation_models


@admin.register(conversation_models.Message)
class MessageAdmin(admin.ModelAdmin):

    """ Message Admin Definition """

    pass


@admin.register(conversation_models.Conversation)
class ConversationAdmin(admin.ModelAdmin):

    """ Conversation Admin Definition """

    list_display = (
        "get_participants",
        "count_participants",
        "count_messages",
    )

    filter_horizontal = ("participants",)

    def get_participants(self, obj):
        return obj

    get_participants.short_description = "Participants"
