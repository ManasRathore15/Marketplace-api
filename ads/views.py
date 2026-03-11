from django.shortcuts import render
from .models import Ad
from .serializers import AdSeiralizer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsOwnerReadOlny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .user_serializer import UserSerializer
from django.contrib.auth.models import User


# Create your views here.

class AdListCreateViews(generics.ListCreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSeiralizer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["title", "location", "price"]

    search_fields = ["title", "description", "location"]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AdDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSeiralizer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerReadOlny]


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer