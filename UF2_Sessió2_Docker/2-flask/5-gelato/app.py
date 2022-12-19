from flask import Flask, render_template, request, redirect, url_for

''' Example before the exam: Gelato Shop.
    Example of converting form data to int.
'''

# Al desarrollar una webapp usando Flask,
# el fichero principal se suele llamar 'app.py'.

# 1. Esto es lo primero en un programa Flask.
# --------------------------------------------
module_name: str   = __name__
app:         Flask = Flask(module_name)


# 3. Esto es lo tercero. Escribir las rutas.
#    Las rutas deben estar siempre antes que el punto 2.
# --------------------------------------------

# We do not have a main page.
# We redirect to the icecream page directly.
# --------------------------------------------
@app.route('/')
def index() -> str:

    return redirect(url_for('choose_icecream'))


# Icecream form.
# --------------------------------------------
@app.route('/icecream', methods = ['GET', 'POST'])
def choose_icecream():

    if request.method == 'GET':
        return render_template('icecream.html')

    if request.method == 'POST':
        icecream: str = request.form['icecream']
        quantity: int = int(request.form['quantity'])

        price:    int = 3 # Euros
        total:    int = quantity * price

        return f"Tienes que pagar {total} euros."


# 2. Esto es lo segundo en un programa Flask.
#    Siempre tiene que estar abajo del todo.
#    Usar debug=True para debugar mejor los errores.
# --------------------------------------------
this_module: str = __name__
main_module: str = '__main__'

if this_module == main_module:
    app.run(debug=True)

# --------------------------------------------
