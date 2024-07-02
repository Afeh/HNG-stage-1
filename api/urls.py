from django.urls import path
from . import views

urlpatterns = [
	path('api/hello', views.greeting_api, name='greeting_api'),
]