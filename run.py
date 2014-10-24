#!flask/bin/python
from app import app
from sys import argv

if len(argv) > 1:
	app.run(host='0.0.0.0')	
else:
	app.run(debug = True)
