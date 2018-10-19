import os
import requests
import mobility_dashboard
from geojson import Feature

ROUTE = [
    {"lat": 64.0027441, "long": -22.7066262},
    {"lat": 64.0317168, "long": -22.1092311},
    {"lat": 63.99879, "long": -21.18802},
    {"lat": 63.4194089, "long": -19.0184548},
    {"lat": 63.5302354, "long": -18.8904333},
    {"lat": 64.2538507, "long": -15.2222918},
    {"lat": 64.913435, "long": -14.01951},
    {"lat": 65.2622588, "long": -14.0179538},
    {"lat": 65.2640083, "long": -14.4037548},
    {"lat": 66.0427545, "long": -17.3624953},
    {"lat": 65.659786, "long": -20.723364},
    {"lat": 65.3958953, "long": -20.9580216},
    {"lat": 65.0722555, "long": -21.9704238},
    {"lat": 65.0189519, "long": -22.8767959},
    {"lat": 64.8929619, "long": -23.7260926},
    {"lat": 64.785334, "long": -23.905765},
    {"lat": 64.174537, "long": -21.6480148},
    {"lat": 64.0792223, "long": -20.7535337},
    {"lat": 64.14586, "long": -21.93955},
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
