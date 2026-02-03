from .models import Learn_rset
from rest_framework import serializers

# Create serializer here.

class Learn_restSerializer(serializers.ModelSerializer):
    class Meta:
        model = Learn_rset
        fields = '__all__'
