# https://hackersandslackers.com/flask-sqlalchemy-database-models/
# https://realpython.com/primer-on-jinja-templating/

from flask import Flask, render_template, send_file, escape, url_for

app = Flask(__name__)


@app.route('/')
def render_index():
    return render_template('index.html')


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/ens')
def ens():
    return render_template('ens.html')

@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run()
