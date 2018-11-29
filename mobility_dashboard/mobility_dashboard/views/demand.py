import flask
import mobility_dashboard
from mobility_dashboard import model
import json
import os

@mobility_dashboard.app.route('/demand/', methods=['GET'])
def show_demand():
    geo = read_demands()
    # _demands()
    return flask.render_template("demand.html", demand_data=geo)

def read_demands():
    geo = {}
    with open('./mobility_dashboard/static/aa_demands.geojson', 'r') as geojson_file:
        geo = json.load(geojson_file)
    return geo

def _demands():
    geo = {}
    with open('./mobility_dashboard/static/demands.geojson', 'r') as geojson_file:
        geo = json.load(geojson_file)
    new_geo = {"type": "FeatureCollection", "crs": { "type": "name", "properties": { "name": "Ann Arbor Demands" } }, "features": []}
    with open('./mobility_dashboard/static/centroids.csv', 'r') as csv_file:
        next(csv_file)
        i = 0
        for line in csv_file:
            line = line.strip()
            geo["features"][i]['geometry']['coordinates'][0] = line.split(',')[1]
            geo["features"][i]['geometry']['coordinates'][1] = line.split(',')[2]
            geo["features"][i]['properties']['id'] = line.split(',')[0]
            # del geo["features"][i]['properties']['tsunami']
            # del geo["features"][i]['properties']['felt']
            new_geo["features"].append(geo["features"][i])
            i += 1
    with open('./mobility_dashboard/static/aa_demands.geojson', 'w+') as new_geojson_file:
        r = json.dumps(new_geo)
        new_geojson_file.write(str(r))
    return new_geo
