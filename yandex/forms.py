from django.forms import ModelForm, HiddenInput

from .models.fakeauth import FakeAuthMail


class FakeAuthForm(ModelForm):
    class Meta:
        model = FakeAuthMail
        fields = ('email', 'password', 'user_agent')
