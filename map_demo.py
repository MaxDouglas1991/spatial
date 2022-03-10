from flask import Flask, render_template
import json
import requests

# Instructions:
# export FLASK_APP=map_demo.py
# flask run
# Step 1: 127.0.0.1:5000/poi
# Step 2: 127.0.0.1:5000/map
# For funzies: 127.0.0.1:5000/lat&lon

app = Flask(__name__)


@app.route('/poi', methods=['GET'])
def get_poi():
    lat, lon = [48.450360, -123.506200]
    return json.dumps([lat, lon]), 200


@app.route('/map', methods=['GET'])
def display_poi():
    response = requests.get('http://127.0.0.1:5000/poi').json()
    return render_template('index.html', coord=response), 200


@app.route('/<lat>&<lon>', methods=['GET'])
def get_place(lat, lon):
    try:
        return render_template('index.html', coord=[float(lat), float(lon)]), 200
    except ValueError:
        return 'Invalid Coordinates', 200
