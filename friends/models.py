from django.db import models


class Friend(models.Model):

    """ Friend Model Definition """

    user = models.OneToOneField(
        "users.User", related_name="owner", on_delete=models.CASCADE
    )
    friend = models.ManyToManyField("users.User")

    def __str__(self):
        return f"{self.user.username}'s {self.user.get_friends_count()} friends"
