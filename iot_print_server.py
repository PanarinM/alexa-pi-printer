#!flask/bin/python

from flask import Flask, request
from escpos.printer import Usb

p = Usb(0x0416, 0x5011)
app = Flask(__name__)

# CREATE 'INDEX' PAGE
@app.route('/')
def index():
    return 'Your Flask server is working!'

# CREATE 'LIST' PAGE FOR PRINTING SHOPPING LIST
@app.route('/list')
def list():

    # REQUEST DATA FROM WEBHOOKS, CONVERT TO STRING AND SPLIT BY LINES
    content = str(request.get_data()).splitlines()

    # SEPERATE WORDS BY COMMA THEN REMOVE FORMATTING MARKS
    rmv_marks = [
	    map(
		    lambda x: x.strip("b'"), 
		    word.split(','),
	    ) for word in content
    ]

    # PRINT HEADER
    # print("Shopping List\n")
    p.text("Shopping List:\n")

    # ENUMERATE AND PRINT EACH ITEM IN LIST
    for num, val in enumerate(rmv_marks, start=1):
	    # print("{}. {}\n".format(num, val))
	    p.text("{}. {}\n".format(num, val))

    return 'x'

# CREATE 'TO DO' PAGE FOR PRINTING TO DO LIST
@app.route('/todo')
def list():
    content = str(request.get_data()).splitlines()
    rmv_marks = [
	    map(
		    lambda x: x.strip("b'"), 
		    word.split(','),
	    ) for word in content
    ]
    p.text("Shopping List:\n")
    for num, val in enumerate(rmv_marks, start=1):
	    p.text("{}. {}\n".format(num, val))
    return 'x'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
