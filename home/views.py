from rest_framework import viewsets
from .models import Banar
from .serializers import BanarSerializer

class BanarViewSet(viewsets.ModelViewSet):
    queryset = Banar.objects.all()
    serializer_class = BanarSerializer
