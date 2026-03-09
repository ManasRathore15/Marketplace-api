from django.shortcuts import render
from .models import Ad
from .serializers import AdSeiralizer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerReadOlny


# Create your views here.

class AdListCreateViews(generics.ListCreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSeiralizer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AdDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSeiralizer
    permission_classes = [IsAuthenticated, IsOwnerReadOlny]