from rest_framework import serializers
from .models import Superhero


class SuperherosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Superhero
        fields = ("name", "alias", "Species", "Date_of_Birth", "Age", "Gender", "intelligence", "strength", "speed", "durability", "power", "combat", "tier")