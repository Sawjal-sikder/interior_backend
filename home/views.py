from rest_framework import viewsets
from .models import *
from .serializers import *

class BanarViewSet(viewsets.ModelViewSet):
    queryset = Banar.objects.all()
    serializer_class = BanarSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
