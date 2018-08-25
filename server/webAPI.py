import sqlite3
from flask import Flask, jsonify, request, abort
from argparse import ArgumentParser

DB = 'API.sqlite'

def get_row_as_dict(row):
	row_dict = {
		'id' : row[0],
		'state' : row[1],
		'location' : row[2],
		'name' : row[3],
		'address' : row[4],
		'description' : row[5],

	}

	return row_dict

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return """<p>WORKING!</p>"""


@app.route('/api/places/', methods=['GET'])
def index():
	db = sqlite3.connect(DB)
	cursor = db.cursor()
	cursor.execute('SELECT * FROM places ORDER BY id')
	rows = cursor.fetchall()

	print(rows)

	db.close()

	rows_as_dict = []
	for row in rows:
		row_as_dict = get_row_as_dict(row)
		row_as_dict.append(row_as_dict)

	return jsonify(row_as_dict), 200

@app.route('/api/places/state/', methods=['GET'])
def HomeScreen():
	db= sqlite3.connect(DB)
	cursor = db.cursor()
	cursor.execute('SELECT state FROM places')
	row = cursor.fetchall()
	db.close()

	return jsonify(row), 200
@app.route('/api/places/state/view/', methods=['GET'])
def ViewScreen():
	db= sqlite3.connect(DB)
	cursor = db.cursor()
	cursor.execute('SELECT (location || " " || name) AS expr1 FROM places')
	row = cursor.fetchall()
	db.close()

	return jsonify(row), 200
@app.route('/api/places/state/detail/', methods=['GET'])
def DetailScreen():
	db= sqlite3.connect(DB)
	cursor = db.cursor()
	cursor.execute('SELECT (location || " " || name || " " || address || " " || description) AS expr1 FROM places')
	row = cursor.fetchall()
	db.close()

	return jsonify(row), 200

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    app.run(host='0.0.0.0', port=port)
