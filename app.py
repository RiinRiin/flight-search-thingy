from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import csv, json
from csv2json import make_json
 
csvFilePath = r'data/flights.csv'
jsonFilePath = r'data/flights.json'
make_json(csvFilePath, jsonFilePath)

with open(jsonFilePath) as fp:
    json_data = json.load(fp)

app = Flask(__name__)
CORS(app)

@app.route('/api/flights')
@cross_origin()
def flights():
    return jsonify(json_data)

@app.route('/api/<station>')
@cross_origin()
def flight_station(station):
    json_data_dict = {}
    for rows in json_data:
        key = rows['id']
        json_data_dict[key] = rows
    flights = []
    for flight in json_data_dict.values():
        if station.lower() in flight["destination"].lower() or station.lower() in flight["destination_full_name"].lower() or station.lower() in flight["origin"].lower() or station.lower() in flight["origin_full_name"].lower():
            flights.append(flight)
    return jsonify(flights)

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