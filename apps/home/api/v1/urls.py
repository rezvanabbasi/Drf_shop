from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.home.api.v1.api import HomeViewSet

app_name = "home"

router = DefaultRouter()
router.register('home', HomeViewSet, basename='home')

urlpatterns = [
    path('', include(router.urls)),
]
