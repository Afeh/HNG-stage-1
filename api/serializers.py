from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
	client_ip = serializers.CharField(max_length=20)
	location = serializers.CharField(max_length=50)
	greeting = serializers.CharField(max_length=255)