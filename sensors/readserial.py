import os
import sys
import serial

while True:
    with serial.Serial('/dev/ttyACM0', 9600) as ser:
        while True:
            line = ser.readline()
            print(line)
