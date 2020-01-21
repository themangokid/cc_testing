
from flask import Flask
app = Flask(__name__)

# this userpass assumes you did not create a password for your database
# and the database username is the default, 'root'

from flask_sqlalchemy import SQLAlchemy

my_attempt = 'mysql://root:root@localhost:8889/Customer'

app.config['SQLALCHEMY_DATABASE_URI'] = my_attempt
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


@app.route('/')
def testdb():
    try:
        # Dubbelkolla så att du har en connection igen.
        print(db.session)
        return '<h1>It works.</h1>'

    except:
        return '<h1>Something is broken<h1>'


if __name__ == '__main__':
    app.run(debug=True)