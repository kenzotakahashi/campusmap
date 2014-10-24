 #!/usr/bin/python
 # -*- coding: utf-8 -*-
from app import app, db
from flask import send_file, jsonify, abort, request


@app.route('/')
def index():
	# Initial Load
    return send_file("templates/index.html")

@app.route('/api/v1/direction/<building>/<int:roomNumber>/<entrance>', methods=['GET'])
def direction(building, roomNumber, entrance):
	# find a room by room number
	building = db.building.find_one({'name': building})
	r = db.room.find_one({'building': building['_id'], 'number': roomNumber})
	# get the entrance and direction
	e = next(x for x in r['direction'] if x['entrance'] == entrance)
	roomDirection = db.direction.find_one({'_id': e['elevator']['direction']})['list']
	roomDirection = [db.phrase.find_one({'_id': id})['phrase'] for id in roomDirection]

	# get the elevator
	elevator = db.elevator.find_one({'_id': e['elevator']['reference']})

	# The room is located in the same floor as the entrance.
	if elevator['floor'] == r['floor']:
		return jsonify({'direction': roomDirection})

	# get the entrance and direction
	e2 = next(x for x in elevator['direction'] if x['entrance'] == entrance)
	elevatorDirection = db.direction.find_one({'_id': e2['direction']})['list']
	elevatorDirection = [db.phrase.find_one({'_id': id})['phrase'] for id in elevatorDirection]

	return jsonify({'direction': elevatorDirection + getFloor(r['floor']) + roomDirection})


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
	professors = [[r['professor'], db.building.find_one({'_id': r['building']})['name'], r['number']] \
					for r in db.room.find() if r['professor'] != '']
	return jsonify({'professors': professors})






# def findByEntrance(lyst, entrance):
# 	return next(x for x in lyst if x['entrance'] == entrance)

