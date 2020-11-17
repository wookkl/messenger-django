from django.db import models


class Comment(models.Model):

    """ Comment Model Definition """

    comment = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="comments", on_delete=models.CASCADE
    )
    likes = models.PositiveIntegerField()
