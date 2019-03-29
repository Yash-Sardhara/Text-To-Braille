import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

servo = GPIO.PWM(21, 50)
servoY = GPIO.PWM(13, 500)
servoX = GPIO.PWM(18, 500)
servo.start(5) # Set Center
sleep(1)

char_num = 0
line_num = 0


def punchHole ():
    for i in range (0,55):
        servo.ChangeDutyCycle(5 + i/10)
        sleep(0.02)
    sleep(0.5)
    for i in range (0,55):
        servo.ChangeDutyCycle(10.5 - i/10)
        sleep(0.04)


def moveLeft ():
    servoX.start(25)
    sleep(0.002)
    servoX.stop()
    sleep(0.002)

def moveUp():
    servoY.start(25)
    sleep(0.002)
    servoY.stop()
    sleep(0.002)
    #servoY.stop()
def moveRight():
    servoX.start(5)
    sleep(0.002)
    servoX.stop()
    sleep(1)
def moveDown():
    servoY.start(10)
    sleep(0.002)
    servoY.stop()
    sleep(0.002)

def printChar(charArray):
    global char_num, line_num
    if charArray[0]:
        punchHole()
    moveLeft()
    if charArray[1]:
        punchHole()
    moveDown()
    if charArray[3]:
        punchHole()
    moveRight()
    if charArray[2]:
        punchHole()
    moveDown()
    if charArray[4]:
        punchHole()
    moveLeft()
    if charArray[5]:
        punchHole()
    char_num = char_num + 1
    if (char_num == 13):
        next_line()
        char_num = 0
        line_num = line_num + 1
    else :
        moveNextChar()
        
def moveNextChar():
    moveLeft()
    moveLeft()
    moveUp()
    moveUp()
    
def next_line():
    global line_num
    
    for i in range(0, char_num - 1):
        moveRight()
        moveRight()
        moveRight()
        
    if line_num == 3:
        for i in range(0, 14) :
            moveUp()
    else:
        moveDown()
        moveDown()

#charArray = [0,1,1,1,0,1]
#printChar(charArray)

#punchHole()
moveLeft()
punchHole()
sleep(1)
moveDown()
punchHole()
sleep(1)
moveRight()
punchHole()
sleep(1)
moveRight()
punchHole()
sleep(1)
#moveUp()
#punchHole()
servo.stop()
