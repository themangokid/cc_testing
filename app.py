
# https://hackersandslackers.com/flask-sqlalchemy-database-models/
from flask import Flask, escape, url_for, render_template, send_file
app = Flask(__name__)

#lade till flask, send_file

#@app.route("/")
#def main():
#    return '''Flask installed.  '''



@app.route('/')
def get_image():
    filename = 'kitten.jpg'
    return send_file(filename, mimetype='kitten.jpg')



@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == "__main__":
    app.run()
