 #!/usr/bin/python
 # -*- coding: utf-8 -*-
from app import app, db
from flask import send_file, jsonify, abort, request


@app.route('/')
def index():
	# Initial Load
    return send_file("templates/index.html")

@app.route('/api/v1/direction/<int:roomNumber>/<entrance>', methods=['GET'])
def direction(roomNumber, entrance):
	# find a room by room number
	r = db.room.find_one({'number': roomNumber})
	# get the entrance and direction
	e = next(x for x in r['direction'] if x['entrance'] == entrance)
	# roomDirection = '\n'.join(db.direction.find_one({'_id': e['elevator']['direction']})['list']) + '\n'
	roomDirection = db.direction.find_one({'_id': e['elevator']['direction']})['list']

	# get the elevator
	elevator = db.elevator.find_one({'_id': e['elevator']['reference']})
	# get the entrance and direction
	e2 = next(x for x in elevator['direction'] if x['entrance'] == entrance)
	# elevatorDirection = '\n'.join(db.direction.find_one({'_id': e2['direction']})['list']) + '\n'
	elevatorDirection = db.direction.find_one({'_id': e2['direction']})['list']

	# return 'room number is: ' + str(room) + ' and entrance is: ' + entrance + '\n'
	return jsonify({'direction': elevatorDirection + roomDirection})






# def findByEntrance(lyst, entrance):
# 	return next(x for x in lyst if x['entrance'] == entrance)

