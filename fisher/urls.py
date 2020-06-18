from django.urls import path

from .views import FakeAuthView, index


app_name = 'fisher'

urlpatterns = [
    path('auth/', FakeAuthView.as_view(), name='fake_auth'),
    path('', index, name='index'),
]
