from flask import Flask, render_template, request
import sys
import json
from Text_To_Braille import printBrailleNumber

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
    text = request.args.get('text')

    return render_template('translator.html', text = text)

@app.route("/test")
def test():
    c = request.args.get('c')

    return json.dumps(printBrailleNumber(c)) 

@app.route("/getText")
def getText():
    text = request.get_json()
    print(text, file=sys.stderr)
    return text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
