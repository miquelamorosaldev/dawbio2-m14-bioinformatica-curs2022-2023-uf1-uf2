from flask import Flask, Response

'''Flask example v2: Returns HTML.'''

# Flask initialization
# ----------------------------------------------------
module_name: str   = __name__
app:         Flask = Flask(module_name)
# ----------------------------------------------------

# If return type is a string, Flask embeds it into
# a Response object automatically with a content type of 'html'.
# ----------------------------------------------------
@app.route('/')
def index():

    quote: str = "<h1> Quote of the day</h1> Deku (My Hero Academia) says 'Plus Ultra!'"

    return quote


# Main
# ----------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
# ----------------------------------------------------
