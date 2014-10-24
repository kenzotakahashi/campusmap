#Create entrance object


building = {
	'_id': Object_Id('541d7ae6705bd619ddbe9b54'),
	'name': 'Innovative Teaching and Technology Center',
	'entrance': ['N', 'E', 'S']
}

# entrance = {
# 	'building' = Object_Id('541d7ae6705bd619ddbe9b54'),
# 	'name' = 'N',
# 	'floor' = 0
# }

# entrance = {
# 	'building' = Object_Id('541d7ae6705bd619ddbe9b54'),
# 	'name' = 'S',
# 	'floor' = 0
# }

# entrance = {
# 	'building' = Object_Id('541d7ae6705bd619ddbe9b54'),
# 	'name' = 'E',
# 	'floor' = 0
# }

room = {
	'_id': ObjectId('541d8bfd705bd619ddbe9b5b'),
	'number': 305,
	'name': 'Computer Science Department',
	'building': ObjectId('541d7ae6705bd619ddbe9b54'),
	'floor': 3,
	'direction': [
		{
			'entrance': 'N',
			'elevator': {
				'reference': ObjectId('541d7da9705bd619ddbe9b59'),
				'direction': [
					ObjectId('541d7bce705bd619ddbe9b55')
				]		
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
				'direction': ObjectId('541d7bce705bd619ddbe9b55')
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
				'direction': ObjectId('541d7bce705bd619ddbe9b55')
			},
			'stair': {
				'reference': None,
				'direction': None,
			},
			'direction': None
		},
	]

}

elevator = {
	'_id': ObjectId('541d7da9705bd619ddbe9b59'),
	'building': ObjectId('541d7ae6705bd619ddbe9b54'),
	'direction': [
		{'entrance': 'N',
		 'direction': ObjectId('541d7c3f705bd619ddbe9b56')},
		{'entrance': 'S',
		 'direction': ObjectId('541d7c59705bd619ddbe9b57')},
		{'entrance': 'E',
		 'direction': ObjectId('541d7c6d705bd619ddbe9b58')},
	]
}	

# This is a direction from the elevator to ITTC 305.
direction = {
	'_id': ObjectId('541d7bce705bd619ddbe9b55'),
	'list': [
	  ObjectId('543f10fc705bd61bbc2223a4'),
		ObjectId('543f0faa705bd61bbc2223a3'),
		ObjectId('543f10fc705bd61bbc2223a4'),
		ObjectId('543f1142705bd61bbc2223a6'),
		ObjectId('543f1157705bd61bbc2223a7')
	]
}

# north
direction = {
	'_id': ObjectId('541d7c3f705bd619ddbe9b56'),
	'list': [
		ObjectId('543f0faa705bd61bbc2223a3'),
		ObjectId('543f1103705bd61bbc2223a5'),
		ObjectId('5447ea4e705bd601899bbf18')
	]
}

# south
direction = {
	'_id': ObjectId('541d7c59705bd619ddbe9b57'),
	'list': [
		ObjectId('543f0faa705bd61bbc2223a3'),
		ObjectId('543f10fc705bd61bbc2223a4'),
		ObjectId('5447ea4e705bd601899bbf18')
	]
}

# East
direction = {
	'_id': ObjectId('541d7c6d705bd619ddbe9b58'),
	'list': [
		ObjectId('543f0faa705bd61bbc2223a3'),
		ObjectId('5447ea6e705bd601899bbf19')
	]
}

phrase = {
	'phrase': 'Walk straight'
}


'Walk straight'
ObjectId('543f0faa705bd61bbc2223a3')
'Turn right'
ObjectId('543f10fc705bd61bbc2223a4')
'Turn left'
ObjectId('543f1103705bd61bbc2223a5')
'Go down the hall'
ObjectId('543f1142705bd61bbc2223a6')
"It's on the right"
ObjectId('543f1157705bd61bbc2223a7')
"It's on the left"
ObjectId('543f115d705bd61bbc2223a8')
"Take the elevator on right"
ObjectId('5447ea4e705bd601899bbf18')
"Take the elevator on left"
ObjectId('5447ea6e705bd601899bbf19')

