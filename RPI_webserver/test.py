from flask import Flask, render_template, request
# import sys
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
    
@app.route("/forward")
def forward():
    # print("Forward", file=sys.stderr)
    return "Forward"

@app.route("/backward")
def backward():
    # print("Backward", file=sys.stderr)
    return "Backward"

@app.route("/turnRight")
def turn_right():
    # print("turnRight", file=sys.stderr)
    return "Right turn"

@app.route("/turnLeft")
def turn_left():
    # print("turnLeft", file=sys.stderr)
    return  "Left turn"

@app.route("/stop")
def stop():
    # print("stopped", file=sys.stderr)
    return "Stopped"

@app.route("/test")
def test():
    number = request.args.get('num')
    dict = {}
    dict['retnum'] = int(number) * 2
    return json.dumps(dict)

@app.route("/moveJoystick", methods = ['POST'])
# reference: https://www.makeuseof.com/tag/python-javascript-communicate-json/
def moveJoystick():
    # print("moveJoystick", file = sys.stderr)
    data = request.get_json()
    # loop over every row
    # print(data, file=sys.stderr)
    # print("left: " + str(data["motorspeed"][0]) + " right: " + str(data["motorspeed"][0]), file = sys.stderr)
    # print("you're gay", file=sys.stderr)
    # print("myJoystick " + str(x) + " "+ str(y), file=sys.stderr)
    return "moveJoystick"



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
