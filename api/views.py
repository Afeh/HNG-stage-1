from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloSerializer
import requests
import json
from django.conf import settings



def get_temperature(location):
	url = f'http://api.weatherapi.com/v1/current.json?key={settings.API_KEY}&q={location}&aqi=no'
	response_data = requests.get(url).json()

	# print(response_data)
	# response_data = json.loads(response.content)

	weather_condition = response_data['current']['condition']
	weather_temperature = response_data['current']['temp_c']


	weather_description = weather_condition['text']

	return weather_temperature


def get_location(ip_address):
	url = f'https://api.ipgeolocation.io/ipgeo?apiKey={settings.API_KEY2}&ip={str(ip_address)}'
	repsonse_data = requests.get(url).json()

	city = repsonse_data['city']

	return city


@api_view(['GET'])
def greeting_api(request):
	visitor_name = request.GET.get('visitor_name', 'Mark')
	# client_ip = request.META.get('REMOTE_ADDR')
	client_ip_address = requests.get('https://ipinfo.io/?token=5f368389d189b7').json()
	client_ip = client_ip_address['ip']
	print(client_ip)


	location = get_location(client_ip)

	temperature = get_temperature(location)

	response_data = {
		'client_ip': client_ip,
		'location': location,
		'greeting': f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {location}"
	}

	serializer = HelloSerializer(data=response_data)

	if serializer.is_valid():
		return Response(serializer.data)
	else:
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


