import flask
import mobility_dashboard
from mobility_dashboard import model


@mobility_dashboard.app.route('/', methods=['GET'])
def show_index():
    route_data = model.get_route_data()
    stop_locations = model.create_stop_locations_details()
    return flask.render_template("index.html", ACCESS_KEY=mobility_dashboard.app.config['MAPBOX_ACCESS_KEY'], route_data = route_data, stop_locations = stop_locations)
