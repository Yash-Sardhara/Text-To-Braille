import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

servo = GPIO.PWM(21, 50)
servoY = GPIO.PWM(13, 50)
servoX = GPIO.PWM(18, 50)
servo.start(5) # Set Center
sleep(1)


def punchHole ():
    for i in range (0,55):
        servo.ChangeDutyCycle(5 + i/10)
        sleep(0.02)
    sleep(0.6)
    for i in range (0,55):
        servo.ChangeDutyCycle(10.5 - i/10)
        sleep(0.04)

def moveLeft ():
    servoX.start(12)
    sleep(0.02)
    servoX.start(45)
    sleep(0.02)
    servoX.stop() 
  
def moveUp():
    servoY.start(8)
    sleep(0.02)
    servoY.start(45)
    sleep(0.02)
    servoY.stop()
    
def moveNextCharLeft():
    servoX.start(45)
    sleep(0.02)
    servoX.stop()
    sleep(0.02)

def moveNextLine():
    servoY.start(9)
    sleep(0.02)
    servoY.stop()
    sleep(0.02)

def moveRight():
    servoX.start(2)
    sleep(0.02)
    servoX.stop()
    sleep(0.02)

def emptyLineHandler():
    moveUp()
    sleep(0.02)
    moveUp()
    sleep(0.02)
    moveNextLine()
    sleep(0.02)
        
def printLines():
    if len(line3) == 0:
        emptyLineHandler()
    else:
        printLine(line3)
    if len(line2) == 0:
        emptyLineHandler()
    else:
        printLine(line2)
    if len(line1) == 0:
        emptyLineHandler()
    else:
        printLine(line1)
    resetPosition()

def resetPosition():
    print("to be implemented")
    #moves it down to the start

'''
1 0
3 2
5 4
'''
def printLine(line):
    left_count = 0
    dot_num = 4 #always starts at bottom right
    for i in range(3):
        for j in line:
            if (j[dot_num]):
                punchHole()
            moveLeft()
            left_count = left_count + 1
            sleep(0.02)
            if (j[dot_num+1]):
                punchHole()
            moveNextCharLeft()
            sleep(0.02)
        dot_num = dot_num - 2
    reset()
    sleep(0.02)
    moveNextLine()
    sleep(0.02)
    

servo.ChangeDutyCycle(5)

'''
string = "hi how was your day"
def printLines():
    line
#get string -> string to braille -> separate by line #s -> print line 3 -> reset to new line -> print line 2 -> reset to new line -> print line 1 -> reset to beginning
'''



servo.stop()
