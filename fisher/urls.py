from django.urls import path

from .views import FisherView


app_name = 'fisher'

urlpatterns = [
    path('auth/', FisherView.as_view(), name='auth'),
]
