import requests

def reverse_geocode(lat, log):
    sensor = 'false'
    base = "http://maps.googleapis.com/maps/api/geocode/json?"
    params = "latlng={lat},{lon}&sensor={sen}".format(
        lat=lat,
        lon=log,
        sen=sensor
    )
    url = "{base}{params}".format(base=base, params=params)
    response = requests.get(url)
    components = response.json()['results'][0]['address_components']
    country = town = None
    for c in components:
        if "country" in c['types']:
            country = c['long_name']
        if "administrative_area_level_1" in c['types']:
            state = c['short_name']
        if "locality" in c['types']:
            town = c['long_name']
    return "{}, {}, {}".format(town,state,country)

if __name__ == "__main__":
    #latitude = 42.4851
    #longitude = -71.4328
    latitude = 40.1164 
    longitude = -88.2434
    location = reverse_geocode(latitude, longitude)
    print(location)
