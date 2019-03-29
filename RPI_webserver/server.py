from __future__ import print_function
from flask import Flask, render_template, request
import sys
import json
import sys

text = " "
braille = "default"
printerBusy = False

app = Flask(__name__)

# Renders the default homepage
@app.route("/")
def index():
    return render_template('home.html')

# Renders the home page when accessing home.html
@app.route("/home.html")
def home():
    return render_template('home.html')

# Renders the dictionary page when accessing dictionary.html
@app.route("/dictionary.html")
def dictionary():
    return render_template('dictionary.html')

# Renders the translator page when accessing translator.html
@app.route("/translator.html")
def translator():
    return render_template('translator.html')

# Renders the game page when accessing game.html
@app.route("/game.html")
def game():
    return render_template('game.html')

# URL that allows client to send a text in a query
@app.route("/sendBraille")
def sendBraille():
    global text
    text = request.args.get('text')
    return text

# URL that passes the text variable into javascript through returning a JSON format
@app.route("/updateText")
def updateText():
    print(text, file=sys.stderr)
    return json.dumps(text)

# (GET) URL that passes the braille variable into javascript thorugh returning a JSON format
# (POST) receives the braille variable from javascript 
@app.route("/getText", methods=['POST', 'GET']) 
def getText():
    global braille
    if request.method == 'POST':
        global printerBusy
        braille = request.get_json()["input"]
        print(braille, file=sys.stderr)
        print(printerBusy, file=sys.stderr)
        printerBusy = True
        return "POST"
    elif request.method == 'GET':
        return json.dumps(braille)
    else:
        return "WTF"

# URL that returns a Boolean representing whether the printer is currently Busy
@app.route("/printerStatus", methods=['GET'])
def printerStatus():
    return json.dumps(printerBusy)

# URL that allows the server to update the printerBusy status to allow the server to know that the print
# job is complete
@app.route("/printJobComplete")
def printJobComplete():
    global printerBusy, braille
    printerBusy = False
    braille = "default"
    return "Printer Idle"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
