import flask
import flask_mail
import jwt

app = flask.Flask(__name__)

app.config["SECRET_KEY"] = 'ShHhHhhhitsasecret'
app.config['MAIL_SERVER'] = 'smtp@gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = "Some App"
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = "jfrance00@gmail.com"
app.config['MAIL_PASSWORD'] = "*****"

payload = {'message': 'helloooo'}
token = jwt.encode(payload, 'ShHhHhhhitsasecret')
print('encoded token: ' + token)

decoded = jwt.decode(token, app.config['SECRET_KEY'])
print(decoded)


print(payload)



mail_mgr = flask_mail.Mail(app)

from . import views
