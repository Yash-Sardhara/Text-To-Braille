from flask import Flask, render_template, request
# import sys
import json

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

@app.route("/test")
def test():
    number = request.args.get('num')
    dict = {}
    dict['retnum'] = int(number) * 2
    return json.dumps(dict)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
