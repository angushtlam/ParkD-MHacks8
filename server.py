from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)


@app.route('/')
def render_index():
    return render_template("index.html")


@app.route('/about')
def render_about():
    return render_template("about.html")


@app.route('/map')
def render_map():
    return render_template("map.html")


@app.route('/api/lot/all')
def api_lot_all():
    with open("carpark_data.json") as f:
        return json.dumps(json.loads(f.read()))


@app.route('/api/lot/nearby')
def api_lot_surrounding():
    with open("foursquare_data.json") as f:
        return json.dumps(json.loads(f.read())["results"])



@app.route('/api/map')
def api_map():
    output_data = {
        "response": "ok",
        "message": "data is valid"
    }

    return json.dumps(output_data)


if __name__ == "__main__":
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.secret_key = "mHaCkZ8"
    app.run(host='0.0.0.0', port=port, debug=True)
