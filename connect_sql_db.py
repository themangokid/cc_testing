from datetime import datetime
from flask import render_template
import pypyodbc
from datetime import datetime
from flask import render_template, redirect, request

# creating connection Object which will contain SQL Server Connection
connection = pypyodbc.connect('Driver={SQL Server};Server=.;Database=Employee;uid=sa;pwd=sA1234')  # Creating Cursor

"""
HAR INGEN ANING OM VAD SOM HÄNDER HÄR DETTA ÄR COPY PASTE:AD KOD. KAN VARA BRA KAN VARA DÅLIG.
"""




cursor = connection.cursor()
cursor.execute("SELECT * FROM EmployeeMaster")
s = "<table style='border:1px solid red'>"
for row in cursor:
    s = s + "<tr>"
for x in row:
    s = s + "<td>" + str(x) + "</td>"
s = s + "</tr>"

connection.close()


@app.route('/')
@app.route('/home')
def home():
    return "<html><body>" + s + "</body></html>"