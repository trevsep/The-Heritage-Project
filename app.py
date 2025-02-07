#Trevor
import re
from datetime import datetime
#import flask
from flask import Flask
#create an instance of the flask object
app = Flask(__name__)
#using app.route decorator to map the URL route / to the function
@app.route('/')
#Create function that returns a string
def name():
    return "Please enter your name: "


#add a new route
@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    #string format time using format codes
    #%A: full weekday name
    #%d: Day of the month
    #%B full month name
    #%y year
    #%x local time representation 
    formatted_now = now.strftime("%A, %d %B, %y at %x")

    #filter the name argument to letters only using regular expressions.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:   
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content

