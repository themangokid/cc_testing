
# https://hackersandslackers.com/flask-sqlalchemy-database-models/
from flask import Flask, escape, url_for, render_template
app = Flask(__name__)


@app.route("/")
def main():
    return '''Flask installed.  '''


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == "__main__":
    app.run()
