from django.shortcuts import render
from rest_framework import generics
from .serializers import playerMetrics_serializer
from .models import playerMetrics

class PlayerMertics_View(generics.ListCreateAPIView):
    queryset = playerMetrics.objects.all()
    serializer_class = playerMetrics_serializer
