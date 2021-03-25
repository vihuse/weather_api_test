from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import City
from .serializers import CitySerializer
from django.http import HttpResponse
import requests

OPENWEATHER_API_URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=3d4e6f86cc87aec614964a8b7fee11ad'
CITIES = ['barcelona', 'paris', 'dubai', 'amsterdam', 'luanda', 'montreal', 'jakarta', 'istanbul', 'cairo', 'singapore']

@api_view(['GET'])
def get_city_by_name(request, name):
    try:
        city = City.objects.get(name=name)
        serializer = CitySerializer(city)
        return Response(serializer.data)
    except City.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_cities(request):
    cities = City.objects.all()
    serializer = CitySerializer(cities, many=True)
    return Response(serializer.data)

def populate_db(request):
    try:
        City.objects.all().delete()
    except:
        pass

    for city in CITIES:
        try:
            response = requests.get(OPENWEATHER_API_URL.format(city)).json()

            city_weather = City(
                name=city,
                temperature=response['main']['temp'],
                description=response['weather'][0]['description'],
            )
            city_weather.save()
        except:
            raise ('City not found!')

    return HttpResponse("Database populated. Check cities weather in: 127.0.0.1:8000/cities/")

def index(request):  
    return HttpResponse("To get data in your Database, go to: 127.0.0.1:8000/populate_db/")