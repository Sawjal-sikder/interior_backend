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
