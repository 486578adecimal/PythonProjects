import serial
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

ser = serial.Serial('COM4', 9600)
def relkeys():
    keyboard.release("w")
    keyboard.release("s")
    keyboard.release("a")
    keyboard.release("d")
print(ser.name)         # check which port was really used
while True:
    key = ser.readline().decode('UTF-8')[0]
    if key == "w":
        relkeys()
        keyboard.press(key)
        print(key)
    elif key == "s":
        relkeys()
        keyboard.press(key)
        print(key)
    elif key == "a":
        relkeys()
        keyboard.press(key)
        print(key)
    elif key == "d":
        relkeys()
        keyboard.press(key)
        print(key)
    elif key == "q":
        relkeys()
        keyboard.press("w")
        keyboard.press("a")
        print("wa")
    elif key == "e":
        relkeys()
        keyboard.press("w")
        keyboard.press("d")
        print("wd")
    elif key == "z":
        relkeys()
        keyboard.press("s")
        keyboard.press("a")
        print("sa")
    elif key == "x":
        relkeys()
        keyboard.press("s")
        keyboard.press("d")
        print("sd")
    else:
        relkeys()

ser.close()
