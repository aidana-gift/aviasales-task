import csv
from flask import Flask, jsonify

app = Flask(__name__)
all_data = {}
with open('schedule.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = {}
    for line in csv_reader:
        data[line['Id']] = line

print(data)

@app.route('/flights', methods=['GET'])
def get_flights():
    return jsonify(data)


@app.route('/flights/<f_id>', methods=['GET'])
def get_by_id(f_id):
    selected = {'Number': data[f_id]['Number'],
                'DepartureTime': data[f_id]['DepartureTime'],
                'ArrivalTime': data[f_id]['ArrivalTime']}
    return jsonify(selected)


if __name__ == '__main__':
    app.run()