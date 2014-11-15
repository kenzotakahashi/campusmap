#Create entrance object


building = {
	'_id': Object_Id('541d7ae6705bd619ddbe9b54'),
	'name': 'Innovative Teaching and Technology Center',
	'entrance': ['N', 'E', 'S']
}

{
	'_id': ObjectId('546281ed705bd652dc718436'),
	'name': 'Wright Hall',
	'entrance': ['NE', 'SE', 'S']
}

{
	'_id': ObjectId('546685a0705bd652dc71843b'),
	'name': 'Russell Hall',
	'entrance': ['N', 'E']
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
				'direction': ObjectId('541d7bce705bd619ddbe9b55')	
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

# ITTC
elevator = {
	'_id': ObjectId('541d7da9705bd619ddbe9b59'),
	'building': ObjectId('541d7ae6705bd619ddbe9b54'),
	'floor': 0,
	'direction': [
		{'entrance': 'N',
		 'direction': ObjectId('541d7c3f705bd619ddbe9b56')},
		{'entrance': 'S',
		 'direction': ObjectId('541d7c59705bd619ddbe9b57')},
		{'entrance': 'E',
		 'direction': ObjectId('541d7c6d705bd619ddbe9b58')},
	]
}	

# Wright Hall
elevator =  {
	'_id': ObjectId('54628628705bd652dc71843a'),
	'building': ObjectId('546281ed705bd652dc718436'),
	'floor': 0,
	'direction': [
		{'entrance': 'NE',
		 'direction': ObjectId('54628556705bd652dc718437')},
		{'entrance': 'SE',
		 'direction': ObjectId('54628588705bd652dc718438')},
		{'entrance': 'S',
		 'direction': ObjectId('546285a7705bd652dc718439')},
	]
}

#  ====== Russel Hall ============================================
elevator = {
	'_id': ObjectId('5466914a705bd652dc718443'),
	'building': ObjectId('546685a0705bd652dc71843b'),
	'floor': 1,
	'direction': [
		{'entrance': 'N',
		 'direction': ObjectId('54668fa8705bd652dc71843f')},
		{'entrance': 'E',
		 'direction': ObjectId('54668fc1705bd652dc718440')}
	]
}

stair = {
	'_id': ObjectId('5466916b705bd652dc718444'),
	'building': ObjectId('546685a0705bd652dc71843b'),
	'floor': 1,
	'direction': [
		{'entrance': 'N',
		 'direction': ObjectId('54668fd3705bd652dc718441')},
		{'entrance': 'E',
		 'direction': ObjectId('54668ff6705bd652dc718442')}
	]
}

# =========== Wright Hall ==============================

# North East
direction = {
	'_id': ObjectId('54628556705bd652dc718437'),
	'list': [
		ObjectId('543f0faa705bd61bbc2223a3'),
		ObjectId('543f1103705bd61bbc2223a5'),
		ObjectId('543f0faa705bd61bbc2223a3'),
		ObjectId('543f1103705bd61bbc2223a5'),
		ObjectId('5447ea4e705bd601899bbf18')	
	]
}

# South East
direction = {
	'_id': ObjectId('54628588705bd652dc718438'),
	'list': [
		ObjectId('543f0faa705bd61bbc2223a3'),
		ObjectId('5447ea6e705bd601899bbf19')
	]
}

# South
direction = {
	'_id': ObjectId('546285a7705bd652dc718439'),
	'list': [
		ObjectId('543f0faa705bd61bbc2223a3'),
		ObjectId('543f10fc705bd61bbc2223a4'),
		ObjectId('5447ea4e705bd601899bbf18')
	]
}

# ================ Russel Hall =======================

# Elevator from North 
direction = {
	'_id': ObjectId('54668fa8705bd652dc71843f'),
	'list': [
		ObjectId('543f10fc705bd61bbc2223a4'),
		ObjectId('543f0faa705bd61bbc2223a3'),
		ObjectId('543f1103705bd61bbc2223a5'),
		ObjectId('5447ea6e705bd601899bbf19')
	]
}

# Elevator from East 
direction = {
	'_id': ObjectId('54668fc1705bd652dc718440'),
	'list': [
		ObjectId('543f10fc705bd61bbc2223a4'),
		ObjectId('543f0faa705bd61bbc2223a3'),
		ObjectId('543f1103705bd61bbc2223a5'),
		ObjectId('543f0faa705bd61bbc2223a3'),
		ObjectId('5447ea6e705bd601899bbf19')		
	]
}

# Stair from North 
direction = {
	'_id': ObjectId('54668fd3705bd652dc718441'),
	'list': [
		ObjectId('54668c5e705bd652dc71843c')
	]
}

# Stair from East
direction = {
	'_id': ObjectId('54668ff6705bd652dc718442'),
	'list': [
		ObjectId('543f10fc705bd61bbc2223a4'),
		ObjectId('543f0faa705bd61bbc2223a3'),
		ObjectId('54668da4705bd652dc71843e'),
		ObjectId('54668c82705bd652dc71843d')
	]
}

# ===============================================

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

# ============== ITTC ===================================

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
# =======================================================

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
"Take the elevator on the right"
ObjectId('5447ea4e705bd601899bbf18')
"Take the elevator on the left"
ObjectId('5447ea6e705bd601899bbf19')
"Take the stair on the right"
ObjectId('54668c5e705bd652dc71843c')
"Take the stair on the left"
ObjectId('54668c82705bd652dc71843d')
"Go down the hallway"
ObjectId('54669c1d705bd652dc718445')
"It's straight ahead"
ObjectId('5449adb7705bd601c3dc8ebb')
