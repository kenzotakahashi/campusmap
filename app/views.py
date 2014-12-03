 #!/usr/bin/python
 # -*- coding: utf-8 -*-
from app import app, db
from flask import send_file, jsonify, abort, request


@app.route('/')
def index():
	# Initial Load
    return send_file("templates/index.html")


def getFloor(floor):
	return ['Go to the ' + ['ground','1st','2nd','3rd','4th'][floor] + ' floor']



@app.route('/api/v1/entrance/<building>', methods=['GET'])
def entrance(building):
	return jsonify({'entrance': db.building.find_one({'name': building})['entrance']})


@app.route('/api/v1/rooms/<building>', methods=['GET'])
def rooms(building):
	rooms = [r['number'] for r in db.room.find({'building': db.building.find_one({'name': building})['_id']})]
	return jsonify({'rooms': rooms})


@app.route('/api/v1/professor', methods=['GET'])
def professor():
	# list of professors along with the building and the room number
	professors = []
	for r in db.room.find():
		if r['professor'] != '':
			if type(r['professor']) == unicode:
				professors.append([r['professor'], db.building.find_one({'_id': r['building']})['name'], r['number']])
			else:
				for p in r['professor']:
					professors.append([p, db.building.find_one({'_id': r['building']})['name'], r['number']])

	# professors = [[r['professor'], db.building.find_one({'_id': r['building']})['name'], r['number']] \
	# 				for r in db.room.find() if r['professor'] != '']
	return jsonify({'professors': sorted(professors, key=lambda x: x[0])})

def breakDown(r):
	"""Break down professors who belong to the same room"""
	return []


@app.route('/api/v1/direction/<building>/<int:roomNumber>', methods=['GET'])
def direction(building, roomNumber):
	# find a room by room number
	building = db.building.find_one({'name': building})
	r = db.room.find_one({'building': building['_id'], 'number': roomNumber})
	# get the entrance and direction
	return jsonify({'direction': [directionByEntrance(r,e) for e in r['direction']]})

def directionByEntrance(r, e):

	# print r['direction'][0]['elevator']['reference']

	# elevator
	if r['direction'][0]['elevator']['reference']:
		roomDirection = db.direction.find_one({'_id': e['elevator']['direction']})['list']
		roomDirection = [db.phrase.find_one({'_id': id})['phrase'] for id in roomDirection]
		# get the elevator
		stair_elevator = db.elevator.find_one({'_id': e['elevator']['reference']})
	# stair
	else:
		roomDirection = db.direction.find_one({'_id': e['stair']['direction']})['list']
		roomDirection = [db.phrase.find_one({'_id': id})['phrase'] for id in roomDirection]
		# get the stair
		stair_elevator = db.stair.find_one({'_id': e['stair']['reference']})

	# The room is located in the same floor as the entrance.
	if stair_elevator['floor'] == r['floor']:
		return {'entrance': e['entrance'], 'direction': roomDirection}

	# get the entrance and direction
	e2 = next(x for x in stair_elevator['direction'] if x['entrance'] == e['entrance'])
	elevatorDirection = db.direction.find_one({'_id': e2['direction']})['list']
	elevatorDirection = [db.phrase.find_one({'_id': id})['phrase'] for id in elevatorDirection]

	return {'entrance': e['entrance'], 'direction': elevatorDirection + getFloor(r['floor']) + roomDirection}

