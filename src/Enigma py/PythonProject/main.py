import serial
import time

ArduinoSerial = serial.Serial('com8',9600)
time.sleep(2)
print(ArduinoSerial.readline())
print ("Enter 1 to turn ON LED and 0 to turn OFF LED")

while 1:
    var = input()
    print ("you entered", var)

    if (var == '1'):
        ArduinoSerial.write(str.encode('1'))
        print ("LED turned ON")
        time.sleep(1)

    if (var == '0'):
        ArduinoSerial.write(str.encode('0'))
        print ("LED turned OFF")
        time.sleep(1)

