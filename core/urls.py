from django.urls import path, include
# from rest_framework import routers
from .views import test_view

# router = routers.DefaultRouter()
# router.register('test', test_view())


urlpatterns = [
    # path('', include(router.urls)),
    path('', test_view)
]
