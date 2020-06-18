from django.db import models


class Victim(models.Model):
    email       = models.CharField(max_length=100)
    password    = models.CharField(max_length=100)

    def __str__(self):
        return self.email
