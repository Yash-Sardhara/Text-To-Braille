from __future__ import print_function
from flask import Flask, render_template, request
import sys
import json
from Text_To_Braille import printBrailleSentence
import sys

text = "(Default)"

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
    # toUpdate["text"] = text
    return json.dumps(text)

@app.route("/test")
def test():
    c = request.args.get('c')
    # return json.dumps(printBrailleNumber(c))
    return json.dumps(braille)

@app.route("/getText", methods = ['POST']) 
def getText():
    global braille
    text = request.get_json()['input']
    print(text, file=sys.stderr)
    braille = printBrailleSentence(text)
    print(braille, file=sys.stderr)
    return "text"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
