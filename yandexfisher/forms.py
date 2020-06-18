from django.forms import ModelForm

from .models import Victim


class FakeAuthForm(ModelForm):
    class Meta:
        model = Victim
        fields = ('email', 'password')
