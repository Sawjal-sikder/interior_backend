# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'banars', BanarViewSet, basename='banar')
router.register(r'service', ServiceViewSet, basename='service')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'portfolio', PortfolioViewSet, basename='portfolio')
router.register(r'contactUs', ContactUsViewSet, basename='ContactUs')
router.register(r'Client', ClientViewSet, basename='client')
router.register(r'Review', ReviewViewSet, basename='Review')
router.register(r'LatestProject', LatestProjectViewSet, basename='LatestProject')
router.register(r'Chooseus', ChooseusViewSet, basename='Chooseus')
router.register(r'Gallary', GallaryViewSet, basename='Gallary')

urlpatterns = [
    path('', include(router.urls)),
]
