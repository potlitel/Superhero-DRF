from rest_framework import serializers
from .models import Superhero


class SuperherosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Superhero
        fields = ("name", "alias")