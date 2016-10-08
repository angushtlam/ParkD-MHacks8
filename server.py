from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/')
def render_index():
    return render_template("index.html")


@app.route('/api/map')
def api_map():
    output_data = {
        "response": "ok",
        "message": "data is valid"
    }

    return json.dumps(output_data)


if __name__ == "__main__":
    app.debug = True
    app.run()
