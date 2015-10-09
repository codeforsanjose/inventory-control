from flask import Flask, render_template, request

from inventory_control import storage

app = Flask(__name__)

config = {'host': 'localhost', 
          'user': 'wce',
          'password': 'thispasswordisobjectivelyterrible',
          'db': 'inventory_control'}

engine = storage.StorageEngine(config=config)

#engine._create_tables()


#@app.route('/', methods=['GET','POST'])
def homepage():	

	words = "This is a test of FLASK to make sure variables work"

	components_by_type = ""

	submit = False

	try:
		return render_template("index.html", words=words, comps=components_by_type, submit=submit)
	except Exception, e:
        	return str(e)
"""
def add_component_type():

	#if 'submit' in request.form.values():
	component_type = request.form['userInput']
	
	engine.add_component_type(type_name=component_type)

	blah = request.form['userInput']

	components_by_type = component_type #engine.get_components(component_type=blah)

	submit = True

	return render_template("index.html", words=words, comps=components_by_type, submit=submit)
"""
"""
def get_components_by_type():
	
	if 'ADD' in request.form.values():

		components_by_type = engine.get_components(component_type = request.form['userInput'])

		return render_template("index.html", words=words, comps=components_by_type)
"""
#commented the above because it didn't work


@app.route('/', methods=['POST'])
def add_component_type():

	if 'ADD' in request.form.values():
		component_type = request.form['userInput']
	
		engine.add_component_type(type_name=component_type)
		engine.db.commit()
		import pdb; pdb.set_trace()



def get_components_by_type():
	
	if 'ADD' in request.form.values():

		components_by_type = engine.get_components(component_type = request.form['userInput'])

		return components_by_type

"""

"""
#Enable this for testing on localhost

if __name__ == "__main__":
	app.run(debug = True)
"""



if __name__ == "__main__":
	app.run(debug = True, host='0.0.0.0', port=8080, passthrough_errors=True)


"""


