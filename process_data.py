import xlrd
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client.campusmap

def main():
	fin = './database/Russel 2nd.xlsx'
	book = xlrd.open_workbook(fin)
	sheet = book.sheet_by_index(0)

	for row in range(1, sheet.nrows):
		roomNum = sheet.cell_value(row, 1)

		print int(roomNum)
		# print sheet.cell_value(row, 3)

		directionList = [cleanUp(x) for x in sheet.cell_value(row, 3).split(',')]

		direction = {'list': directionList}

		directionId = db.direction.insert(direction)

		prof = sheet.cell_value(row, 5).split(',')
		professor = prof[0] if len(prof) == 1 else prof

		room = {
			'number': int(roomNum),
			'name': '',
			'professor': professor,
			'building': ObjectId('546685a0705bd652dc71843b'),
			'floor': 2,
			'direction': [
				{
					'entrance': 'N',
					'elevator': {
						'reference': ObjectId('5466914a705bd652dc718443'),
						'direction': directionId
					},
					'stair': {
						'reference': None,
						'direction': None,
					},
					'direction': None
				},
				{
					'entrance': 'E',
					'elevator': {
						'reference': ObjectId('5466914a705bd652dc718443'),
						'direction': directionId
					},
					'stair': {
						'reference': None,
						'direction': None,
					},
					'direction': None
				},
			]

		}

		db.room.insert(room)




	# # ===================== for ground floor =====================================

	# for row in range(1, sheet.nrows):
	# 	roomNum = sheet.cell_value(row, 1)

	# 	if row % 2 == 1: #roomNum != '':
	# 		print int(roomNum)
	# 		# print sheet.cell_value(row, 5)

	# 		directionListN = [cleanUp(x) for x in sheet.cell_value(row, 3).split(',')]
	# 		directionListE = [cleanUp(x) for x in sheet.cell_value(row+1, 3).split(',')]

	# 		directionN = {'list': directionListN}
	# 		directionE = {'list': directionListE}
			
	# 		directionIdN = db.direction.insert(directionN)
	# 		directionIdE = db.direction.insert(directionE)

	# 		prof = sheet.cell_value(row, 5).split(',')
	# 		professor = prof[0] if len(prof) == 1 else prof

	# 		room = {
	# 			'number': int(roomNum),
	# 			'name': '',
	# 			'professor': professor,
	# 			'building': ObjectId('546685a0705bd652dc71843b'),
	# 			'floor': 1, #int(sheet.cell_value(row, 1)),
	# 			'direction': [
	# 				{
	# 					'entrance': 'N',
	# 					'elevator': {
	# 						'reference': ObjectId('5466914a705bd652dc718443'),
	# 						'direction': directionIdN
	# 					},
	# 					'stair': {
	# 						'reference': None,
	# 						'direction': None,
	# 					},
	# 					'direction': None
	# 				},
	# 				{
	# 					'entrance': 'E',
	# 					'elevator': {
	# 						'reference': ObjectId('5466914a705bd652dc718443'),
	# 						'direction': directionIdE
	# 					},
	# 					'stair': {
	# 						'reference': None,
	# 						'direction': None,
	# 					},
	# 					'direction': None
	# 				},
	# 			]

	# 		}

	# 		db.room.insert(room)


def cleanUp(p):
	"""strip off period, capitalize."""

	# p = p.strip()
	# p[0].upper()
	# if p[-1] == '.':
	# 	p = p[:-1]

	# phrase = db.phrase.find_one({'phrase': p.capitalize()})
	# if phrase:
	# 	return phrase['_id']

	# phrase = db.phrase.insert({'phrase': p.capitalize()})
	# return phrase

	if p == 'r': return ObjectId('543f10fc705bd61bbc2223a4')
	if p == 'l': return ObjectId('543f1103705bd61bbc2223a5')
	if p == 's': return ObjectId('543f0faa705bd61bbc2223a3')
	if p == 'g': return ObjectId('54669c1d705bd652dc718445')
	if p == 'R': return ObjectId('543f1157705bd61bbc2223a7')
	if p == 'L': return ObjectId('543f115d705bd61bbc2223a8')
	if p == 'S': return ObjectId('5449adb7705bd601c3dc8ebb')



main()











