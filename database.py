#Create entrance object


building = {
	'_id': Object_Id('541d7ae6705bd619ddbe9b54')
	'name': 'ITTC',
	'entrance': ['N', 'E', 'S']
}

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
					ObjectId('541d7bce705bd619ddbe9b55')
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


direction = {
	'_id': ObjectId('541d7bce705bd619ddbe9b55'),
	'list': [
		'This is a direction from the elevator to ITTC 305.',
		'This is another direction from the elevator to ITTC 305.'
	]
}

direction = {
	'_id': ObjectId('541d7c3f705bd619ddbe9b56'),
	'list': [
		'This is a direction from the north entrance to the elevator.',
		'This is another direction from the north entrance to the elevator.'
	]
}

direction = {
	'_id': ObjectId('541d7c59705bd619ddbe9b57'),
	'list': [
		'This is a direction from the south entrance to the elevator.',
		'This is another direction from the south entrance to the elevator.'
	]
}

direction = {
	'_id': ObjectId('541d7c6d705bd619ddbe9b58'),
	'list': [
		'This is a direction from the east entrance to the elevator.',
		'This is another direction from the east entrance to the elevator.'
	]
}

