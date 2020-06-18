from django.forms import ModelForm

from .models.fakeauth import FakeAuthMail


class FakeAuthForm(ModelForm):
    class Meta:
        model = FakeAuthMail
        fields = ('email', 'password')
