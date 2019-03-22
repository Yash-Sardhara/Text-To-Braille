import RPi.GPIO as GPIO
from collections import defaultdict
import time

padRows= [17,27,22,5] 
padCols= [6,13,19]

keypad = [['1','2','3'],['4','5','6'],['7','8','9'],['*','0','#']] #2D Matrix

GPIO.setmode(GPIO.BCM) #sets board mode
GPIO.setup(padRows[0], GPIO.IN,pull_up_down=GPIO.PUD_UP) #if pressed we will read GPIO.LOW, else GPIO.HIGH if not pressed
GPIO.setup(padRows[1], GPIO.IN,pull_up_down=GPIO.PUD_UP) 
GPIO.setup(padRows[2], GPIO.IN,pull_up_down=GPIO.PUD_UP) 
GPIO.setup(padRows[3], GPIO.IN,pull_up_down=GPIO.PUD_UP) 
GPIO.setup(padCols[0] , GPIO.OUT,initial=GPIO.HIGH) 
GPIO.setup(padCols[1] , GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(padCols[2], GPIO.OUT,initial=GPIO.HIGH)

curr_time = time.time()
start_time = curr_time

capital_flag = 0
number_flag = 0
inputs = []
braille_dictionary = dict([
    ('1', 'a'),
    ('14', 'b'),
    ('12', 'c'),
    ('125', 'd'),
    ('15', 'e'),
    ('124', 'f'),
    ('1245', 'g'),
    ('145', 'h'),
    ('24', 'i'),
    ('245', 'j'),
    ('17', 'k'),
    ('147', 'l'),
    ('127', 'm'),
    ('1257', 'n'),
    ('157', 'o'),
    ('1247', 'p'),
    ('12457', 'q'),
    ('1457', 'r'),
    ('247', 's'),
    ('2457', 't'),
    ('178', 'u'),
    ('1478', 'v'),
    ('2458', 'w'),
    ('1278', 'x'),
    ('12578', 'y'),
    ('1578', 'z')
    ])


def keypad_check():
    global curr_time, start_time
    for j in range (3):
            GPIO.output(padCols[j], GPIO.LOW)
            for i in range (4):
                curr_time = time.time()
                if (curr_time > start_time + 0.35):
                    if (GPIO.input(padRows[i])==GPIO.LOW):
                        start_time = curr_time
                        print (keypad[i][j])
                        return (keypad[i][j])
            GPIO.output(padCols[j], GPIO.HIGH) #turns off the col so that next iteration its not still on
    return '10'
def submit():
    user_input = ""
    for i in inputs:
        user_input = user_input + i
    print(user_input)
    inputs.clear()
    try:
        print((braille_dictionary[user_input]))
    except:
        print ("Not a real braille character")

def braille_to_char():
    input = keypad_check()
    if (input == '10'):
        return
    elif (input == '3'):
        del inputs[-1]
    elif (input == '*'):
        inputs.clear()
    elif (input == '#'):
        submit()
    elif (len(inputs) < 6):
        inputs.append(input)

while True:
    braille_to_char()
