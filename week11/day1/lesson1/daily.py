from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/lesson1')
def lesson():
    return render_template('in-this-chapter.md')


@app.route('/exercises')
def practice():
    return render_template('exercises.md')


if __name__ == '__main__':
    app.run(debug=True)
