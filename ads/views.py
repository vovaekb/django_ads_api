from django.shortcuts import render
from rest_framework import generics
from .models import User, Ad
from .serializers import UserSerializer, AdSerializer

class ListAdsView(generics.ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer