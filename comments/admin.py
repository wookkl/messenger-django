from django.contrib import admin
from comments import models as comment_models


@admin.register(comment_models.Comment)
class CommentAdmin(admin.ModelAdmin):

    """ Comment Admin Definition """

    list_display = (
        "user",
        "pheed",
        "comment",
    )
