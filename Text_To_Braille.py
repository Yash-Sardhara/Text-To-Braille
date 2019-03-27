
outputs = []
def textToBraille (character):
    toBraille = {"a":[1,0,0,0,0,0],
                 "b":[1,0,1,0,0,0],
                 "c":[1,1,0,0,0,0],
                 "d":[1,1,0,1,0,0],
                 "e":[1,0,0,1,0,0],
                 "f":[1,1,1,0,0,0],
                 "g":[1,1,1,1,0,0],
                 "h":[1,0,1,1,0,0],
                 "i":[0,1,1,0,0,0],
                 "j":[0,1,1,1,0,0],
                 "k":[1,0,0,0,1,0],
                 "l":[1,0,1,0,1,0],
                 "m":[1,1,0,0,1,0],
                 "n":[1,1,0,1,1,0],
                 "o":[1,0,0,1,1,0],
                 "p":[1,1,1,0,1,0],
                 "q":[1,1,1,1,1,0],
                 "r":[1,0,1,1,1,0],
                 "s":[0,1,1,0,1,0],
                 "t":[0,1,1,1,1,0],
                 "u":[1,0,0,0,1,1],
                 "v":[1,0,1,0,1,1],
                 "w":[0,1,1,1,0,1],
                 "x":[1,1,0,0,1,1],
                 "y":[1,1,0,1,1,1],
                 "z":[1,0,0,1,1,1],
                 "#":[0,1,0,1,1,1],
                 ";":[0,0,1,0,1,0],
                 ",":[0,0,1,0,0,0],
                 "'":[0,0,0,0,1,0],
                 ".":[0,0,1,1,0,1],
                 "?":[0,0,1,0,1,1],
                 "!":[0,0,1,1,1,0],
                 ":":[0,0,1,1,0,0],
                 "-":[0,0,0,0,1,1],
                 "CAPS":[0,0,0,0,0,1],
                 }
    
    return toBraille[character]

def tempPrint (characterVector) :
    outputs.append(characterVector)
    '''
    print(characterVector[0],characterVector[1])
    print(characterVector[2],characterVector[3])
    print(characterVector[4],characterVector[5])
    print("-----------")
    '''
def printBrailleNumber(character) :
    toBraille = {"1":[1,0,0,0,0,0],
                 "2":[1,0,1,0,0,0],
                 "3":[1,1,0,0,0,0],
                 "4":[1,1,0,1,0,0],
                 "5":[1,0,0,1,0,0],
                 "6":[1,1,1,0,0,0],
                 "7":[1,1,1,1,0,0],
                 "8":[1,0,1,1,0,0],
                 "9":[0,1,1,0,0,0],
                 "0":[0,1,1,1,0,0]
                 }
    return toBraille[character]

def printBraille (word) :
    numUpperCase = 0
    numberStatus = False
        
    for letter in word:
        if letter.isdigit():
            if numberStatus == False :
                numberStatus = True
                tempPrint(textToBraille("#"))
                tempPrint(printBrailleNumber(letter))
            else :
                tempPrint(printBrailleNumber(letter))
        else :
            if numberStatus == True :
                numberStatus = False
                tempPrint(textToBraille(";"))
                tempPrint(textToBraille(letter.lower()))
            else :
                tempPrint(textToBraille(letter.lower()))

def printBrailleSentence (sentence):
    words = sentence.split()
    for word in words:
        printBraille(word)
        #print("@@@@@@@@@@@")

string  = "cpen 291"
printBrailleSentence(string)





    
