import urllib
from urllib.request import urlopen
import json
from time import sleep


class LocationQuery:

    status = ""
    results = None
    fields_dict = {}

    def __init__(self):
        pass

    def gmaps_query(self, address_string):
        if address_string is None or address_string is "":
            return
        attempts = 0
        success = False
        url_data = address_string.replace(" ", "+")  # make links URL friendly.  ex. ' ' becomes '+'
        url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + url_data
        while success is not True and attempts < 3:
            le_data = urllib.request.urlopen(url)
            resp_data = json.loads(str(le_data.read().decode("utf-8")))
            print(resp_data['status'])
            print(resp_data['results'])
            if resp_data['status'] == "OVER_QUERY_LIMIT":
                sleep(2)
                continue
            success = True
        if attempts == 3:
            self.status = resp_data['status']
        self.status = resp_data['status']
        self.results = resp_data['results']

    def gmaps_parse(self, result_choice):
        if result_choice is None or self.status != "OK" or result_choice < 0:
            return
        for field in self.results[result_choice]['address_components']:
            if ("point_of_interest" in field['types']) or ("establishment" in field['types']):
                self.fields_dict['name'] = field['short_name']
            elif "street_number" in field['types']:
                self.fields_dict['street_number'] = field['short_name']
            elif "route" in field['types']:
                self.fields_dict['street'] = field['short_name']
            elif ("locality" in field['types']) and ("political" in field['types']):
                self.fields_dict['city'] = field['long_name']
            elif ("administrative_area_level_2" in field['types']) and ("political" in field['types']):
                self.fields_dict['county'] = field['long_name']
            elif ("administrative_area_level_1" in field['types']) and ("political" in field['types']):
                self.fields_dict['state'] = field['short_name']
            elif ("country" in field['types']) and ("political" in field['types']):
                self.fields_dict['country'] = field['short_name']
            elif "postal_code" in field['types']:
                self.fields_dict['zip'] = field['short_name']
            else:
                continue
        self.fields_dict['lat'] = self.results[result_choice]['geometry']['location']['lat']
        self.fields_dict['lng'] = self.results[result_choice]['geometry']['location']['lng']