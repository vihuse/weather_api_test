import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import City
from ..serializers import CitySerializer

client = Client()

class GetAllCitiesTest(TestCase):
    
    def setUp(self):
        City.objects.create(
            name='moscow', temperature='37.05', description='overcast clouds')
        City.objects.create(
            name='osaka', temperature='58.21', description='broken clouds')
        City.objects.create(
            name='montevideo', temperature='72.01', description='clear sky')
        City.objects.create(
            name='munich', temperature='52.12', description='broken clouds')

    def test_get_all_cities(self):
        response = client.get(reverse('get_cities'))

        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetOneCityTest(TestCase):

    def setUp(self):
        self.moscow = City.objects.create(
            name='moscow', temperature='37.05', description='overcast clouds')
        self.osaka = City.objects.create(
            name='osaka', temperature='58.21', description='broken clouds')
        self.montevideo = City.objects.create(
            name='montevideo', temperature='72.01', description='clear sky')
        self.munich = City.objects.create(
            name='munich', temperature='52.12', description='broken clouds')
        
    def test_get_one_valid_city(self):
        response = client.get(
            reverse('get_city_by_name', kwargs={'name': self.munich.name}))
        city = City.objects.get(name=self.munich.name)
        serializer = CitySerializer(city)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_invalid_city(self):
        response = client.get(
            reverse('get_city_by_name', kwargs={'name': 'chicago'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
