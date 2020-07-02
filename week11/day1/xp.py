import flask


app = flask.Flask(__name__)



@app.route('/cv')
def display_cv():
    template = open('templates/cv.html', 'r').read()
    html_template = flask.render_template_string(template, name="Julie France")
    return html_template




app.run()


