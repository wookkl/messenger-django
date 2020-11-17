from django.db import models


class Friend(models.Model):

    """ Friend Model Definition """

    user = models.OneToOneField("users.User")
    friend = models.ManyToManyField("users.User")
