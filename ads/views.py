from django.shortcuts import render
from .models import Ad
from .serializers import AdSeiralizer
from rest_framework import generics


# Create your views here.

class AdListCreateViews(generics.ListCreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSeiralizer


class AdDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSeiralizer