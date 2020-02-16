from django.urls import path, include
from .views import PostCreateView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', PostCreateView.as_view(), name='test'),
    path('api/token/', obtain_auth_token, name='obtain-token'),
    path('rest-auth/', include('rest_auth.urls'))
]
