from flask import Flask, Response, jsonify

'''My first Flask example returns JSON.'''

# Flask initialization
# ----------------------------------------------------
module_name: str   = __name__
app:         Flask = Flask(module_name)
# ----------------------------------------------------

# Index (root)
# ----------------------------------------------------
@app.route('/')
def index() -> Response:

    data: dict = {'character': 'Deku',
                  'quote':     'Plus Ultra' }

    response: Response = jsonify(data)
    return response


# Main
# ----------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
# ----------------------------------------------------
