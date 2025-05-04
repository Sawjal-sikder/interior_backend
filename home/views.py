from rest_framework import viewsets
from .models import *
from .serializers import *

class BanarViewSet(viewsets.ModelViewSet):
    queryset = Banar.objects.filter(is_active=True)
    serializer_class = BanarSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.filter(is_active=True)
    serializer_class = PortfolioSerializer


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class LatestProjectViewSet(viewsets.ModelViewSet):
    queryset = LatestProject.objects.filter(is_active=True)
    serializer_class = LatestProjectSerializer


class ChooseusViewSet(viewsets.ModelViewSet):
    queryset = Chooseus.objects.filter(is_active=True)
    serializer_class = ChooseusSerializer
