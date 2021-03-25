from django.test import TestCase
from ..models import City

class CityTest(TestCase):

    def setUp(self):
        City.objects.create(
            name='Barcelona', temperature = 55.11, description = 'Sunny')

    def test_get_weather(self):
        barcelona_weather = City.objects.get(name='Barcelona')
        self.assertEqual(
            barcelona_weather.get_weather(), 'Barcelona: 55.11 ºF. Sunny.'
        ) 