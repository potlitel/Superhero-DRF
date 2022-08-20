from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Superhero
from .serializers import SuperherosSerializer


class ListSuperherosView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Superhero.objects.all().order_by('name')
    serializer_class = SuperherosSerializer
    
class ListSuperherosByGenderView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    serializer_class = SuperherosSerializer    
    
    def get_queryset(self):
        """
        This view should return a list of all the superheros filter by the gender portion of the URL.
        """
        gender = self.kwargs['gender']
        return Superhero.objects.filter(Gender=gender).order_by('name')
    