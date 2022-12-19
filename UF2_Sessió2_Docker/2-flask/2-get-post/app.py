import random
from   pathlib import Path
from   flask import Flask, render_template, request

'''Flask example: GET and POST methods.'''

# Flask initialization
# ----------------------------------------------------
module_name: str   = __name__
app:         Flask = Flask(module_name)
root_path:   Path  = Path(app.root_path)
# ----------------------------------------------------

# ----------------------------------------------------
@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        comic:  str = request.form['comic']
        volume: str = request.form['volume']
        return f'You have bought {comic}, volume {volume}'

# Main
# ----------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
# ----------------------------------------------------
