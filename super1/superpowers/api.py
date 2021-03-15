from superpowers.models import SuperPowersModel
from rest_framework import viewsets, permissions
from .serializers import SuperPowersSerializer
 
# SuperInformation views
 
class SuperPowersViewSet(viewsets.ModelViewSet):
    queryset    = SuperPowersModel.objects.all()
    permission_classes  = [
        permissions.AllowAny
    ]
    serializer_class    = SuperPowersSerializer
