from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

from .forms import VictimForm


class FisherView(CreateView):
    model = User
    form_class = VictimForm
    template_name = 'auth.html'
