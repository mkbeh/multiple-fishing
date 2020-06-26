from django.db import models


class FakeAuth(models.Model):
    email       = models.CharField(max_length=100)
    password    = models.CharField(max_length=100)
    user_agent  = models.CharField(max_length=500)

    class Meta:
        abstract = True


class FakeAuthMail(FakeAuth):
    class Meta:
        verbose_name            = 'Mail'
        verbose_name_plural     = 'Mail'

    def __str__(self):
        return self.email
