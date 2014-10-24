import xlrd
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client.campusmap

def main():
	fin = './database/groundfloor.xlsx'
	book = xlrd.open_workbook(fin)
	sheet = book.sheet_by_index(0)

	for row in range(1, sheet.nrows):
		roomNum = sheet.cell_value(row, 1)
		if row % 3 == 0: #roomNum != '':
			print int(roomNum)
			# print sheet.cell_value(row, 3)

			directionListE = [cleanUp(x) for x in sheet.cell_value(row-2, 10).split(',')]
			directionListS = [cleanUp(x) for x in sheet.cell_value(row-1, 10).split(',')]
			directionListN = [cleanUp(x) for x in sheet.cell_value(row, 10).split(',')]

			directionE = {'list': directionListE}
			directionS = {'list': directionListS}
			directionN = {'list': directionListN}
			
			directionIdE = db.direction.insert(directionE)
			directionIdS = db.direction.insert(directionS)
			directionIdN = db.direction.insert(directionN)

			room = {
				'number': int(roomNum),
				'name': '',#sheet.cell_value(row, 3),
				'professor': '', #sheet.cell_value(row, 11),
				'building': ObjectId('541d7ae6705bd619ddbe9b54'),
				'floor': 0, #int(sheet.cell_value(row, 1)),
				'direction': [
					{
						'entrance': 'N',
						'elevator': {
							'reference': ObjectId('541d7da9705bd619ddbe9b59'),
							'direction': directionIdN
						},
						'stair': {
							'reference': None,
							'direction': None,
						},
						'direction': None
					},
					{
						'entrance': 'S',
						'elevator': {
							'reference': ObjectId('541d7da9705bd619ddbe9b59'),
							'direction': directionIdS
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
							'reference': ObjectId('541d7da9705bd619ddbe9b59'),
							'direction': directionIdE
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


def cleanUp(p):
	p = p.strip()
	if p[-1] == '.':
		p = p[:-1]

	phrase = db.phrase.find_one({'phrase': p})
	if phrase:
		return phrase['_id']

	phrase = db.phrase.insert({'phrase': p})
	return phrase

main()

