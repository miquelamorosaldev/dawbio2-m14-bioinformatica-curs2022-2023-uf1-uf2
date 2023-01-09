#!/usr/bin/env python

from flask import Flask, render_template, request, redirect, url_for

''' Example of static files (images) in the templates.
    The Python code here is the same as comics/app3.py.
'''

# Flask initialization (needed for decorators)
#----------------------------------------------------------------------
module_name: str   = __name__
app:         Flask = Flask(module_name)
#----------------------------------------------------------------------


# The root route is usually called 'index'.
#----------------------------------------------------------------------
@app.route('/')
def index() -> str:

    return render_template('index.html')


# GET + POST request. Parameters are in the form.
# Once we get the data from the form, we redirect to the buy URL.
# url_for() gets the name of the FUNCTION. It allows us to change routes easily.
# app.root_path has the path where app.py is located!
#----------------------------------------------------------------------
@app.route('/form', methods=['GET', 'POST'])
def form():

    # El navegador entra por 1a vez, hace un GET y le envío el formulario
    if request.method == 'GET':
        return render_template('form.html')

    # Cuando el usuario rellena el formulario, envía un POST y lo trato aquí    
    if request.method == 'POST':
        comic:  str = request.form['comic']
        volume: str = request.form['volume']

        # Si faltan parámetros volvemos al formulario
        if (not comic) or (not volume):
            return redirect(url_for('form'))
        # Si los parámetros son correctos mostramos la página de pago
        else:
            return redirect(url_for('buy', comic=comic, volume=volume))


# GET request only. Parameters are in the route.
#----------------------------------------------------------------------
@app.route('/buy/<comic>/<volume>')
def buy(comic: str, volume: str) -> str:

    return render_template('bill.html', comic=comic, volume=volume)


# Main
#----------------------------------------------------------------------
this_module: str = __name__
main_module: str = '__main__'

if this_module == main_module:
    app.run(debug = True)

#----------------------------------------------------------------------
