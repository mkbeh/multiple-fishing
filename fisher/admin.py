from django.contrib import admin

from .models import Victim


@admin.register(Victim)
class VictimAdmin(admin.ModelAdmin):
    pass
