# serializers.py

from rest_framework import serializers
from .models import Receipe


class ReceipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipe
        fields = '__all__'
