import flask

app = flask.Flask(__name__)
app.config.from_object('mobility_dashboard.config')
app.config.from_envvar('DASHBOARD_SETTINGS', silent=True)
MAPBOX_ACCESS_KEY = app.config['MAPBOX_ACCESS_KEY']

import mobility_dashboard.views
import mobility_dashboard.model
import os
