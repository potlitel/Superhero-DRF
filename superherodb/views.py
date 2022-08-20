from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Superhero
from .serializers import SuperherosSerializer


class ListSuperherosView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Superhero.objects.all()
    serializer_class = SuperherosSerializer