import flask
import mobility_dashboard
from mobility_dashboard import model


@mobility_dashboard.app.route('/demand/', methods=['GET'])
def show_demand():
    return flask.render_template("demand.html")
