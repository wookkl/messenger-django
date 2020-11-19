from django.db import models
from core.models import TimeStampedModel


class Photo(TimeStampedModel):

    """ Photo Model Definition """

    file = models.ImageField()
    pheed = models.ForeignKey("Pheed", related_name="photos", on_delete=models.CASCADE)


class Pheed(TimeStampedModel):

    """ Pheed Model Definition """

    description = models.TextField(max_length=300)
    likes = models.PositiveIntegerField()
    user = models.ForeignKey(
        "users.User", related_name="pheeds", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user.username}'s Pheed {self.pk}"