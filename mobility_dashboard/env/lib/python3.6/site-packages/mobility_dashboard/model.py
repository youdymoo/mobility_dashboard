import os
import requests
import mobility_dashboard
from geojson import Feature, Point

ROUTE = [
    {"lat": 42.295353, "long": -83.717652, "name": "A1", "is_stop_location": True},
    {"lat": 42.297133, "long": -83.749585, "name": "B1", "is_stop_location": False},
    {"lat": 42.290750, "long": -83.769424, "name": "A2", "is_stop_location": True},
    {"lat": 42.281176, "long": -83.778909, "name": "A3", "is_stop_location": True},
    {"lat": 42.268800, "long": -83.759415, "name": "B2", "is_stop_location": False},
    {"lat": 42.265116, "long": -83.749306, "name": "B3", "is_stop_location": False},
    {"lat": 42.245311, "long": -83.748713, "name": "A4", "is_stop_location": True},
    {"lat": 42.2622588, "long": -83.748112, "name": "A5", "is_stop_location": True},
    {"lat": 42.242383, "long": -83.737498, "name": "A6", "is_stop_location": True},
    {"lat": 42.253445, "long": -83.697748, "name": "B4", "is_stop_location": False},
    {"lat": 42.270639, "long": -83.725687, "name": "B5", "is_stop_location": False},
    {"lat": 42.277922, "long": -83.742615, "name": "A7", "is_stop_location": True},
    {"lat": 42.283456, "long": -83.749112, "name": "A8", "is_stop_location": True},
    {"lat": 42.291613, "long": -83.730212, "name": "A9", "is_stop_location": True},
]

ROUTE_URL = "https://api.mapbox.com/directions/v5/mapbox/driving/{0}.json?access_token={1}&overview=full&geometries=geojson"

def create_route_url():
    # Create a string with all the geo coordinates
    lat_longs = ";".join(["{0},{1}".format(point["long"], point["lat"]) for point in ROUTE])
    # Create a url with the geo coordinates and access token
    url = ROUTE_URL.format(lat_longs, mobility_dashboard.app.config['MAPBOX_ACCESS_KEY'])
    return url

def get_route_data():
    # Get the route url
    route_url = create_route_url()
    # Perform a GET request to the route API
    result = requests.get(route_url)
    # Convert the return value to JSON
    data = result.json()

    # Create a geo json object from the routing data
    geometry = data["routes"][0]["geometry"]
    route_data = Feature(geometry = geometry, properties = {})

    return route_data

def create_stop_locations_details():
    stop_locations = []
    for location in ROUTE:
        # Skip anything that is not a stop location
        if not location["is_stop_location"]:
            continue
        # Create a geojson object for stop location
        point = Point([location['long'], location['lat']])
        properties = {
            'title': location['name'],
            'icon': 'campsite',
            'marker-color': '#3bb2d0',
            'marker-symbol': len(stop_locations) + 1
        }
        feature = Feature(geometry = point, properties = properties)
        stop_locations.append(feature)
    return stop_locations
