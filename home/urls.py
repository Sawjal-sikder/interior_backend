# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'banars', BanarViewSet, basename='banar')
router.register(r'service', ServiceViewSet, basename='service')

urlpatterns = [
    path('', include(router.urls)),
]
