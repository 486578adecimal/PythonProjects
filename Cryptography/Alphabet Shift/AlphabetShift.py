## This is a program that will "Encrypt" data by shifting the position of letters
## by a certain amount.

import time
## First we need to define a list of all the letters in the alphabet.

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numberShift = 5 ## value to determine what we will shift by

## Function to return the index of a letter


def getIndex(letter):
    index = 0
    for i in alphabet:
        index = index + 1
        if i == letter:
            return index


## function to shift a letter by x amount.

def shift(letter):
    isUpper = False
    if letter.isupper():
        isUpper = True
    letter = letter.lower()
    letterIndex = getIndex(letter)
    if letterIndex > 26-numberShift:
        newLetter = alphabet[letterIndex+numberShift-27]
        ##print("Hai")
    else:
        newLetter = alphabet[letterIndex+numberShift-1]
    if isUpper:
        return newLetter.upper()
    else:
        return newLetter
		
## function that will shift backwards a letter by x amount

def deshift(letter):
    isUpper = False
    if letter.isupper():
        isUpper = True
    letter = letter.lower()
    letterIndex = getIndex(letter)
    if letterIndex < numberShift:
        newLetter = alphabet[letterIndex-numberShift+25]
    else:
        newLetter = alphabet[letterIndex-numberShift-1]
    if isUpper:
        return newLetter.upper()
    else:
        return newLetter


def encrypt(text):
    encryptedText = ""
    for i in text:
        temp = i
        if getIndex(temp.lower()):
            temp = shift(temp)
        encryptedText = encryptedText + temp
    return encryptedText

def decrypt(text):
    decryptedText = ""
    for i in text:
        temp = i
        if getIndex(temp.lower()):
            temp = deshift(temp)
        decryptedText = decryptedText + temp
    return decryptedText

def menu():
    print("Encrypt\n\n1.Line of Text\n2.Textfile\n\n\nDecrypt\n\n3.Line of Text\n4.Textfile")
    menuInput = str(input(">: "))
    if menuInput == "1":
        userInput = str(input("Type in a line or a word to be encrypted: "))
        print(encrypt(userInput))
        time.sleep(100)
    elif menuInput == "2":
        print("This will encrypt a text file please name it as 'tbe.txt'")
        file = open("tbe.txt","r")
        encryptedData = encrypt(file.read())
        file.close()
        file = open("e.txt","w")
        file.write(encryptedData)
        time.sleep(100)
    elif menuInput == "3":
        userInput = str(input("Type in a line or word to be decrypted: "))
        print(decrypt(userInput))
        time.sleep(100)
    elif menuInput == "4":
        print("This will decrypt a text file please name it as 'tbde.txt'")
        file = open("tbde.txt","r")
        decryptedData = decrypt(file.read())
        file.close()
        file = open("de.txt","w")
        file.write(decryptedData)
        time.sleep(100)
    else:
        print("Not a valid menu option")
        time.sleep(100)

menu()
