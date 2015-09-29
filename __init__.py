from flask import Flask, render_template, request

from inventory_control import storage

app = Flask(__name__)

config = {'host': 'localhost', 'user': 'wce',
              'password': 'thispasswordisobjectivelyterrible',
              'db': 'inventory_control'}

#Logs into the database and allows for use of:    engine.[StorageEngine child function]
engine = storage.StorageEngine(config=config)

#This currently throws an error when tables are already created.
#engine._create_tables()



@app.route('/')
def homepage():
	
	#This is for testing variable passing to templates
	variable = "working"

	try:
		#first "variable" is the variable name in the .html
		#second "variable" is the name of the variable in this file
		return render_template("index.html", variable=variable) 
	except Exception, e:
        	return str(e)



#Enable this for testing on localhost
if __name__ == "__main__":
	app.run(debug = True)


"""
#Enbale this for broadcast on webserver.
if __name__ == "__main__":
	app.run(debug = True, host='0.0.0.0', port=8080, passthrough_errors=True)
"""



















