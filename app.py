from flask import Flask, render_template, request, g

from inventory_control import storage

app = Flask(__name__)

config = {'host': 'localhost',
          'user': 'wce',
          'password': 'thispasswordisobjectivelyterrible',
          'db': 'inventory_control'}


def _get_engine():
    return storage.StorageEngine(config=config)


@app.before_first_request
def create_tables():
    _get_engine()._create_tables()


@app.before_request
def create_engine():
    g.engine = _get_engine()


@app.teardown_request
def destroy_engine(exception):
    engine = getattr(g, 'engine', None)
    if engine:
        engine.db.commit()
        engine.db.close()


@app.route('/', methods=['GET', 'POST'])
def homepage():
    words = "This is a test of FLASK to make sure variables work"

    components_by_type = ""

    submit = False

    if request.method == 'GET':
        try:
            resp = render_template("index.html", words=words,
                                   comps=components_by_type, submit=submit)
            return resp
        except Exception, e:
            return str(e)
    else:
        return add_component_type()


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

# def get_components_by_type():

#     if 'ADD' in request.form.values():

#         components_by_type = engine.get_components(component_type = request.form['userInput'])

#         return render_template("index.html", words=words, comps=components_by_type)

#commented the above because it didn't work


def add_component_type():

    if 'ADD' in request.form.values():
        component_type = request.form['userInput']
        with g.engine.db:
            g.engine.add_component_type(type_name=component_type)


# def get_components_by_type():

#     if 'ADD' in request.form.values():

#         components_by_type = engine.get_components(component_type = request.form['userInput'])

#         return components_by_type

"""

"""
#Enable this for testing on localhost

if __name__ == "__main__":
    app.run(debug = True)
    """



if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port=8080, passthrough_errors=True)


"""
