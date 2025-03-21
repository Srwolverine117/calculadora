from flask import Flask

app = Flask(__name__)


@app.route('/wellcome/<name>')
#def home(name):
def hello(name):
    return '¡Bienvenido a mi aplicación Flask!' + name

@app.route('/wellcome/<int:ncontrol>')
def hello_int(ncontrol):
    return f'¡Bienvenido a mi aplicación Flask! Tu número de control es: {ncontrol}'

@app.route('/wellcome/<nombre>/<int:ncontrol>')
def hello_nombre_int(ncontrol, nombre):
    return f'¡Bienvenido a mi aplicación Flask! Tu número de control es: {ncontrol} y tu nombre es: {nombre}'

@app.route('/wellcome/')

@app.route('/wellcome/<name>')

@app.route('/wellcome/<int:ncontrol>')

@app.route('/wellcome/<name>/<int:ncontrol>')

def bienvenido(name=None,ncontrol=None):

    if name== None and ncontrol==None:

        return 'Bienvenido '

    if name!= None and ncontrol == None:

        return f'Bienvenido {name}'

    if name == None and ncontrol != None:

        return f'El número recibido es: {ncontrol}'

    else:

        return f'Bienvenido {name} tu numero de control es: {ncontrol}'




#http://127.0.0.1:5000/wellcome/Daniel Serrano

#http://127.0.0.1:5000/wellcome/03490102

#http://127.0.0.1:5000/wellcome/Daniel Serrano/03490102



