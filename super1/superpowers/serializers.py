from rest_framework import serializers
from superpowers.models import SuperPowersModel
 
class SuperPowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperPowersModel
        fields = '__all__'