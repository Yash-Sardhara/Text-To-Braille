from __future__ import print_function
from flask import Flask, render_template, request
import sys
import json
from Text_To_Braille import printBrailleSentence
import sys

text = "(Default)"
braille = "default"

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/home.html")
def home():
    return render_template('home.html')

@app.route("/dictionary.html")
def dictionary():
    return render_template('dictionary.html')

@app.route("/translator.html")
def translator():
    return render_template('translator.html')

@app.route("/game.html")
def game():
    return render_template('game.html')

@app.route("/sendBraille")
def sendBraille():
    global text
    text = request.args.get('text')
    return text

@app.route("/updateText")
def updateText():
    print(text, file=sys.stderr)
    return json.dumps(text)

@app.route("/getText", methods=['POST', 'GET']) 
def getText():
    global braille
    if request.method == 'POST':
        braille = request.get_json()["input"]
        print(braille, file=sys.stderr)
        return "POST"
    elif request.method == 'GET':
        return json.dumps(braille)
    else:
        return "WTF"

@app.route("/printJobComplete")
def printJobComplete():
    braille = "default"
    return "Printer Idle"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
