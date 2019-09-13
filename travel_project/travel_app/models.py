from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from geopy.geocoders import Nominatim

def get_lats(address):
    geolocator = Nominatim(user_agent="cwelzbazooka@gmail.com")
    value =  geolocator.geocode(address)
    lats = value.latitude
    return lats

def get_longs(address):
    geolocator = Nominatim(user_agent="cwelzbazooka@gmail.com")
    value =  geolocator.geocode(address)
    lons = longitude
    return lons



class Single_Localisation(models.Model):
    title = models.CharField(max_length=70)
    address = models.CharField(max_length=100)
    len_of_stay = models.FloatField()
    description = models.CharField(max_length=150)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.now) 
    lat = get_lats(address)
    lon = get_longs(address)

    # geolocator = Nominatim(user_agent="cwelzbazooka@gmail.com")
    # value =  geolocator.geocode(address)
    # lats = value.latitude
    # lons = value.longitude

    # def coordinates(self):
    #     geolocator = Nominatim(user_agent="travel_app")
    #     lon = geolocator.geocode(self.address).longitude
    #     lat = geolocator.geocode(self.address).latitude
    #     return lon, lat

    def __str__(self):
        return self.title
