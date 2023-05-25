from django.db import models


class Game(models.Model):
    uid = models.CharField(max_length=20)
