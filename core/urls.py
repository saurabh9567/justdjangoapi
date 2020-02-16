from django.urls import path
from .views import TestView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', TestView.as_view(), name='test'),
    path('api/token/', obtain_auth_token, name='obtain-token'),
]
