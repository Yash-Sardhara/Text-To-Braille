import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

servo = GPIO.PWM(18, 50)
servo.start(7.5) # Set Center
sleep(1)

def punchHole ():
    for i in range (0,10):
        servo.ChangeDutyCycle(7.5 - i/10)
        sleep(0.01)
    for i in range (10,0):
        servo.ChangeDutyCycle(7.5 - i/10)
        sleep(0.01)


                                                   
punchHole()
servo.stop()
GPIO.cleanup()
