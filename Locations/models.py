from django.db import models
from django.utils.translation import gettext as _

from utils import generate_id
import math


class LocationManager(models.Manager):
    def get_distance(self, loc):
        """
        Gets the distance between two locations.
        """
        lat_a = self.lat
        lng_a = self.long
        lat_b = loc.lat
        lng_b = loc.long

        R = 6371
        dLat = math.radians(math.fabs(lat_b-lat_a))
        dLon = math.radians(math.fabs(lng_b-lng_a))
        lat1 = math.radians(lat_a)
        lat2 = math.radians(lat_b)

        a = math.sin(dLat/2) * math.sin(dLat/2) + math.sin(dLon/2) * math.sin(dLon/2) * math.cos(lat1) * math.cos(lat2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        distance = R * c
        return distance

    def name_for(self, name):
        return self.filter(name__icontains=name)

    def street_for(self, street1_name, street2_name):
        return self.filter(street1__iexact=street1_name, street2__iexact=street2_name)

    def city_for(self, city_name):
        return self.filter(city__iexact=city_name)

    def state_for(self, state_name):
        return self.filter(state__iexact=state_name)

    def country_for(self, country_name):
        return self.filter(country__iexact=country_name)

    def zip_for(self, zip_name):
        return self.filter(zip=zip_name)


class Location(models.Model):
    """
    Creates the model of the Location object(s).
    """
    int_uuid = generate_id.int_uuid()
    slug = models.SlugField(default=str(int_uuid), max_length=100, unique=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    street_num = models.CharField(max_length=36)
    street1 = models.CharField(max_length=250)
    street2 = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=36)
    country = models.CharField(max_length=36)
    zip = models.CharField(max_length=36)
    lat = models.FloatField()
    lng = models.FloatField()

    objects = models.Manager()
    loc_manager = LocationManager()
