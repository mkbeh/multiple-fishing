from django.forms import ModelForm
from django.contrib.auth.models import User


class VictimForm(ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
