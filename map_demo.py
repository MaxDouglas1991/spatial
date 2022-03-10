from flask import Flask, render_template
import json
import requests

# export FLASK_APP=map_demo.py
# flask run
# 127.0.0.1:5000/
app = Flask(__name__)


def get_address():
    # my_address = 'street=206 Concordia Place'
    my_address = 'street=1342 Hillside Ave'

    url = f'https://nominatim.openstreetmap.org/search/{my_address}?format=json'
    # url = f'https://nominatim.openstreetmap.org/lookup/{my_address}?format=json'
    print(url)

    response = requests.get(url).json()
    print(response)
    if response:
        if 'lat' in response[0] and 'lon' in response[0]:
            print(response[0]["lat"])
            print(response[0]["lon"])


@app.route('/poi', methods=['GET'])
def get_poi():
    lang, long = [49.161071, -123.974091]
    return json.dumps([lang, long]), 200


@app.route('/map', methods=['GET'])
def display_poi():
    return render_template('index.html', coord=[49.1615323, -123.97471761]), 200


@app.route('/<lat>&<lon>', methods=['GET'])
def get_place(lat, lon):
    return render_template('index.html', coord=[float(lat), float(lon)]), 200


# response = requests.get('127.0.0.1:5000/poi').json()
# print(response)