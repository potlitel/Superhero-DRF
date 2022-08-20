from django.urls import reverse
from rest_framework.views import status
from rest_framework.test import APITestCase, APIClient

from superherodb.serializers import SuperherosSerializer
from .models import Superhero

# Create your tests here.


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_superhero(name="", alias="", Species="", Date_of_Birth="", Age="", Gender="", intelligence="", strength="", speed="", durability="", power="", combat="", tier=""):
        if name != "" and alias != "" and Species != ""and Date_of_Birth != ""and Gender != ""and intelligence != ""and strength != ""and speed != ""and durability != ""and power != ""and combat != "" and tier != "":
            Superhero.objects.create(name=name, alias=alias, Species=Species, Date_of_Birth=Date_of_Birth, Age=Age, Gender=Gender, intelligence=intelligence, strength=strength, speed=speed, durability=durability, power=power, combat=combat, tier=tier)

    def setUp(self):
        # add test data
        self.create_superhero("Lucifer Morningstar", "A","Before the creation of the Universe", "13.8+ Billion Years Old","M", 95,100, 100,100, 100, 100, 100, 9)
        self.create_superhero("Lucifer Morningstar1", "A","Before the creation of the Universe", "13.8+ Billion Years Old","M", 95,100, 100,100, 100, 100, 100, 9)
        self.create_superhero("Lucifer Morningstar2", "A","Before the creation of the Universe", "13.8+ Billion Years Old","M", 95,100, 100,100, 100, 100, 100, 9)
        self.create_superhero("Lucifer Morningstar3", "A","Before the creation of the Universe", "13.8+ Billion Years Old","M", 95,100, 100,100, 100, 100, 100, 9)


class GetAllSuperheroTest(BaseViewTest):

    def test_get_all_superheros(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("superheros-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Superhero.objects.all()
        serialized = SuperherosSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
