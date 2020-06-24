from django.urls import path

from .views import FakeAuthView, index, logo, return_back, registration, forgot_login, forgot_pwd, social, help


app_name = 'yandex'

urlpatterns = [
    path('help', help, name='help'),
    path('social/<str:social_network_name>', social, name='social'),
    path('forgot_pwd', forgot_pwd, name='forgot_pwd'),
    path('forgot_login', forgot_login, name='forgot_login'),
    path('registration', registration, name='registration'),
    path('auth/return_back', return_back, name='return_back'),
    path('auth/logo', logo, name='logo'),
    path('auth/', FakeAuthView.as_view(), name='fake_auth'),
    path('', index, name='index'),
]
