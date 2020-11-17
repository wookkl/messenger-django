from django.db import models


class Friend(models.Model):

    """ Friend Model Definition """

    user = models.OneToOneField("users.User", related_name="friends")
    friend = models.ManyToManyField("users.User", related_name="friends")
