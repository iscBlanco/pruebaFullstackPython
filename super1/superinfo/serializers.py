from rest_framework import serializers
from superinfo.models import SuperInformation

class SuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperInformation
        fields = '__all__'