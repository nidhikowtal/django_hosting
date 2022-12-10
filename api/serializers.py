from rest_framework.serializers import ModelSerializer
from .models import farmer

class farmerSerializer(ModelSerializer):
    class Meta:
        model=farmer
        fields='__all__'
