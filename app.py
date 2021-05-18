from flask import Flask, request, jsonify
import csv, json
from csv2json import make_json
 
csvFilePath = r'data/flights.csv'
jsonFilePath = r'data/flights.json'
make_json(csvFilePath, jsonFilePath)

with open(jsonFilePath) as fp:
    json_data = json.load(fp)
# json_formatted_str = json.dumps(json_data, indent=2)


app = Flask(__name__)

@app.route('/api/flights')
def flights():
    return json.dumps(json_data, indent=2)

@app.route('/api/<station>')
def flight_station(station):
    flights = {}
    for flight in json_data.values():
        if flight["destination"] == station or flight["destination_full_name"] == station or flight["origin"] == station or flight["origin_full_name"] == station:
            flights[flight["id"]] = flight
    return json.dumps(flights, indent=2)


# @app.route('/api/<flight_id>')
# def flight_id(flight_id):
#     if flight_id in json_data:
#         result = json_data[flight_id]
#     else:
#         result = "Flight id Not found"
#     return json.dumps(result, indent=2)


# @app.route('/api/<flight_id>/<station>')
# def flight_station(flight_id, station):
#     if station in json_data[flight_id]["destination"] or json_data[flight_id]["destination_full_name"] or json_data[flight_id]["origin"] or json_data[flight_id]["origin_full_name"]:
#         result = json_data[flight_id]
#     else:
#         result = "Station Not found"
#     return json.dumps(result, indent=2)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
    