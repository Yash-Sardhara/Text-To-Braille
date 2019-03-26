from flask import Flask, render_template, request, redirect, Response
from adafruit_motorkit import MotorKit
import threading
import RPi.GPIO as GPIO
import time
from adafruit_motorkit import MotorKit
import Adafruit_CharLCD as LCD
import sys
from twython import Twython
import picamera

'''
Authors: G-12, L2A

Backend server for running the web app from a specific IP. Features directional inputs, a joystick, and a speed slider
Implmented using Flask
'''

ledR = 14
ledL = 15

GPIO.setup(ledR, GPIO.OUT)
GPIO.setup(ledL, GPIO.OUT)

MAINFUNC = 0
WEB = 1

app = Flask(__name__)
kit = MotorKit()

baseSpeed2 = 0.5
state = WEB

#sets up robot and sensors (refer to lcdddddd.py)
robot = MotorKit()
OSensor1= 26
OSensor2 = 21
OSensor3 = 19

prevStates = []
# Raspberry Pi pin configuration:
lcd_rs        = 20  
lcd_en        = 16
lcd_d4        = 25
lcd_d5        = 23
lcd_d6        = 24
lcd_d7        = 18
lcd_backlight = 4

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                          lcd_columns, lcd_rows, lcd_backlight)

#intializes all values that were used in lcddddddd.py for the main functionality
startTime= time.time()
currTime=startTime

#left 26
#middle 19
#right 21

GPIO.setmode(GPIO.BCM)

GPIO.setup(OSensor1,GPIO.IN)
GPIO.setup(OSensor2,GPIO.IN)
GPIO.setup(OSensor3,GPIO.IN)

#initialize these variables
kP = 0.41
kI = 0.0
kD = 0.45

previousError = 0
currentError = 0
Integral = 0
Differential = 0
beginningTime = time.time()

baseSpeed = 0.41
turnSpeed = 0.41
endLine=False

STRAIGHT = 0
LEFT = 1
RIGHT = 2
STOP = 3



#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)
#
## set up pin numbers for LEDs
#leftTurn = 1
#rightTurn = 2
#frontled = 3
#powerOn = 4
#
## initialize LEDs
#GPIO.setup(leftTurn, GPIO.OUT)
#GPIO.setup(rightTurn, GPIO.OUT)
#GPIO.setup(frontled1, GPIO.OUT)
#GPIO.setup(frontled2, GPIO.OUT)
#GPIO.setup(powerOn, GPIO.OUT)

#GPIO.setup(frontled1, GPIO.HIGH)
#GPIO.setup(frontled2, GPIO.HIGH)

#on setup, make sure robot does not move
def setup():
    stop()

paused = True
#function for stopping the robot
def pause():
#    GPIO.output(rightTurn, GPIO.LOW)
#    GPIO.output(leftTurn, GPIO.LOW)
    global paused
    paused = False
    kit.motor1.throttle = 0
    kit.motor2.throttle = 0

#function for going forward/backward
def drive(forward):
    global baseSpeed2
    if(forward == True):
        kit.motor1.throttle = baseSpeed2
        kit.motor2.throttle = baseSpeed2

    else:
#        GPIO.output(leftTurn, GPIO.HIGH)
#        #GPIO.setup(rightTurn, GPIO.HIGH)
        kit.motor1.throttle = -baseSpeed2
        kit.motor2.throttle = -baseSpeed2

#function for turns
def turn(clockwise):
    global baseSpeed2
    if(clockwise == False):
        kit.motor1.throttle = baseSpeed2
        kit.motor2.throttle = -baseSpeed2
    else:
#        GPIO.output(leftTurn, GPIO.HIGH)
        kit.motor1.throttle = -baseSpeed2
        kit.motor2.throttle = baseSpeed2

#function for variable motor values
def moveAround(l, r):
    kit.motor2.throttle = l
    kit.motor1.throttle = r
    print("moveAround", file = sys.stderr)

#defines the syntax for recieving files from the server
@app.route("/")
def index():
    return render_template('index.html')

'''
All of the following functions are received from the server and call the above functions to carry out the movement.
The server sends a signal that is recevied as "/forward" and then the functions in the server execute the requested
motion.
'''
@app.route("/forward")
def forward():
    drive(True)
    print("Forward", file=sys.stderr)
    return "Forward"

@app.route("/backward")
def backward():
    drive(False)
    print("Backward", file=sys.stderr)
    GPIO.output(ledR, GPIO.HIGH)
    GPIO.output(ledL, GPIO.HIGH)
    return "Backward"

@app.route("/turnRight")
def turn_right():
    turn(True)
    print("turnRight", file=sys.stderr)
    GPIO.output(ledR, GPIO.HIGH)
    return "Right turn"

@app.route("/turnLeft")
def turn_left():
    turn(False)
    print("turnLeft", file=sys.stderr)
    GPIO.output(ledL, GPIO.HIGH)
    return  "Left turn"

@app.route("/stop")
def stop():
    pause()
    print("stopped", file=sys.stderr)
    GPIO.output(ledR, GPIO.LOW)
    GPIO.output(ledL, GPIO.LOW)
    return "Stop"

'''
This is for our joystick, capable of 360 degree directional influence. It recieves an array of values for the left and right motor
which are sent as json files and calls the moveAround function to execute the desired motion
'''
@app.route("/moveJoystick", methods = ['POST'])
# reference: https://www.makeuseof.com/tag/python-javascript-communicate-json/
def moveJoystick():
    print("moveJoystick", file = sys.stderr)
    data = request.get_json()
    # loop over every row
        # for item in data:
        #     left = item['l']
        #     right = item['r']

    print("left: " + str(data["motorspeed"][0]) + " right: " + str(data["motorspeed"][0]), file = sys.stderr)
    moveAround(data["motorspeed"][0], data["motorspeed"][1])

    # print("myJoystick " + str() + " "+ str(y), file=sys.stderr)
    return "moveJoystick"


#takes as parameters the function call and an array with the slider value of the base speed which is used for the speed for all functions
#controlled by the LCD
@app.route("/changeBaseSpeed", methods = ['POST'])
def changeBaseSpeed():
    global baseSpeed2
    print("changeBasespeed", file = sys.stderr)
    speed = request.get_json()
    baseSpeed2 = speed["baseSpeed"][0]
    return "changeBaseSpeed"



#updates the LCD with the appropriate direction (ONLY FOR MAIN FUNCTIONALITY)
def updateLCD(direction):
    lcd.clear()
    
    if (direction == LEFT):
        lcd.message('TURNING LEFT <--')
    elif (direction == RIGHT):
        lcd.message('TURNING RIGHT ->')
    elif (direction == STOP):
        stop_message = "REACHED END: " + str(int(time.time()-beginningTime)) + "s"
        lcd.message(stop_message)
    else:
        lcd.message('MOVING FORWARD  ')

#executes main functionality when requested by server (PLEASE READ lcdddddd.py for info on this function)
def mainfunc():
    global state
    print("went into main", file=sys.stderr)
    while True:
        if state == MAINFUNC:
            print("running",file=sys.stderr)
            global previousError,currentError, Integral,currTime,startTime,endLine,start
            previousError = currentError
            print("state: main fun 1", file=sys.stderr)
            currentReading = - GPIO.input(OSensor1) + GPIO.input(OSensor3)

            Integral = currentReading + Integral
            Differential = currentReading - previousError
            currentError = kP*currentReading + kI*Integral + kD*Differential
            
            if currentError == 0 :
                speedR = baseSpeed
                speedL = baseSpeed
            else :
                speedR = turnSpeed - 0.5 * currentError
                speedL = turnSpeed + 0.5 * currentError
            
            if speedR < -1:
                speedR = -1
            elif speedR > 1:
                speedR = 1

            if speedL > 1 :
                speedL = 1
            elif speedL < -1:
                speedL = -1
                
            try: 
                robot.motor1.throttle = speedR
                robot.motor2.throttle = speedL
            except:
                print("Ran into error", file=sys.stderr)
                mainfunc()   


            if currentError < 0:
                prevStates.append(LEFT)
            elif currentError > 0:
                prevStates.append(RIGHT)
            else:
                prevStates.append(STRAIGHT)


            if len(prevStates) > 6:
                del prevStates[0]

            currTime = time.time()
            if (currTime > startTime + 0.5):
                startTime = currTime
                l = 0
                r = 0
                s = 0
                
                for state2 in prevStates:
                    if state2 == LEFT:
                        l = l + 1
                    elif state2 == RIGHT:
                        r = r + 1
                    else:
                        s = s + 1
                if l > r:
                    updateLCD(LEFT)
                elif r > l:
                    updateLCD(RIGHT)
                else:
                    updateLCD(STRAIGHT)

            if GPIO.input(OSensor1) + GPIO.input(OSensor2) + GPIO.input(OSensor3) == 0:
                if endLine == False:
                    endLine =True
                    start = time.time()
                    print("reading all zero", file=sys.stderr)

                if endLine == True and time.time() - start > 1.3:
                    robot.motor1.throttle = 0
                    robot.motor2.throttle = 0
                    updateLCD(STOP)
                    #breaks out of main functionality loop
                    print("we out", file=sys.stderr)
                    state = WEB
            else:
                endLine = False

        
#starts server
if __name__ == "__main__":
    setup()
    # p1 = Process(target = main)
    # p1.start()
    # p2 = Process(target = changeState)
    # p2.start()
    app.run(host='0.0.0.0', port=80, debug=True)


# p1 = threading.Thread(name='main func', target=mainfunc)
# p1.start()

'''
Changes state between the web app and the main functionality
'''
@app.route("/changeState", methods = ['POST'])
def changeState():
    global state
    global firsttime
    global startTime
    print("changeState", file = sys.stderr)
    data = request.get_json()
    state = data["states"][0]
    if state == MAINFUNC:
        startTime = time.time()
        print("state: main fun", file=sys.stderr)
    else:
        print("state: remote", file=sys.stderr)
        pause()
    return "changeState"

