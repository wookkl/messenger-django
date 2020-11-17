from django.db import models


class Friend(models.Model):

    """ Friend Model Definition """

    user = models.OneToOneField(
        "users.User", related_name="friends", on_delete=models.CASCADE
    )
    friend = models.ManyToManyField("users.User")
