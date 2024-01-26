# api_views.py

from rest_framework import generics
from .models import Receipe
from .serializers import ReceipeSerializer


class ReceipeListCreateView(generics.ListCreateAPIView):
    queryset = Receipe.objects.all()
    serializer_class = ReceipeSerializer


class ReceipeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Receipe.objects.all()
    serializer_class = ReceipeSerializer
