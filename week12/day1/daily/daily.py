import flask
import flask_wtf
import wtforms
import json

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'shhh_its_a_secret'


class Resume(flask_wtf.FlaskForm):
    full_name = wtforms.StringField("Full Name")
    email = wtforms.StringField("Email")
    address = wtforms.StringField("Address")
    phone = wtforms.StringField("Phone Number")
    last_job = wtforms.StringField('Most recent position, company')
    past_job = wtforms.StringField('Past positions (separated by ","')
    skills = wtforms.StringField('Skills ( separated by ","')
    submit = wtforms.SubmitField("Make Resume")



@app.route('/', methods=['GET', 'POST'])
def home():
    form = Resume()
    if flask.request.method == "POST":
        name = form.full_name.data
        email = form.email.data
        address = form.address.data
        phone = form.phone.data
        last_job = form.last_job.data
        cv_content = {'name': name, 'email': email, 'address': address, 'phone': phone, 'last': last_job}
        json.dump(cv_content, open('package.json', 'w'))

    else:
        return flask.render_template('home.html', form=form)


@app.route('/resume', methods=['GET', 'POST'])
def resume():
    return flask.render_template('resume.html')


if __name__ == '__main__':
    app.run(debug=True)
