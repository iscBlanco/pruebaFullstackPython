from superinfo.models import SuperInformation
from rest_framework import viewsets, permissions
from .serializers import SuperSerializer

# SuperInformation views

class SuperViewSet(viewsets.ModelViewSet):
    queryset    = SuperInformation.objects.all()
    permission_classes  = [
        permissions.AllowAny
    ]
    serializer_class    = SuperSerializer