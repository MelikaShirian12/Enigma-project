# import serial
# import time
#
#
# ArduinoSerial = serial.Serial('com7', 9600)
# time.sleep(2)
# print(ArduinoSerial.readline())
# print("Enter 1 to turn ON LED and 0 to turn OFF LED")
#
# while 1:
#     var = input()
#     print("you entered", var)
#
#     if (var == '1'):
#         ArduinoSerial.write(str.encode('1'))
#         print("LED turned ON")
#         time.sleep(1)
#
#     if (var == '0'):
#         ArduinoSerial.write(str.encode('0'))
#         print("LED turned OFF")
#         time.sleep(1)
from collections import deque



class Code:

    def __int__(self, date, rotor1, rotor2, rotor3, plugboard, reflector):
        self.date = date
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3
        self.plugboard = plugboard
        self.reflector = reflector




class MyMap:

    def __init__(self):
        self.table = []


    def hash_function(self,keyCharacters, valueCharacters):

        keyCharacters = list(keyCharacters)
        valueCharacters = list(valueCharacters)


        for i in range(len(keyCharacters)):
            new_entry = Entry(keyCharacters[i], valueCharacters[i])
            self.table.append(new_entry)


        return self.table


    def rotation(self):
        self.table =deque(self.table)
        #rotating it to the right one time
        self.table.rotate(1)


    def find_value(self , key):

        for entry in self.table:
            if entry.key == key:
                return entry

    def find_key(self, value):

        for entry in self.table:
            if entry.value == value:
                return entry


class Entry:

    def __init__(self, key, value):
        self.key = key
        self.value = value
class Files:

    def getData(self, date):
        code_info = list()
        check = False

        file = open('D:\\university\\programs-data struct\\github projects\\enigma pro\\Enigma-project\\Files\\EnigmaFile.txt')
        for line in file:
            if line.startswith('Date: ' + date):
                check = True
                continue
            if check and line.startswith('PlugBoard:'):
                code_info.append(line[line.find('[') + 1: line.find(']')])
            elif check and line.startswith('Rotor1:'):
                code_info.append(line[line.find('[') + 1: line.find(']')])
            elif check and line.startswith('Rotor2:'):
                code_info.append(line[line.find('[') + 1: line.find(']')])
            elif check and line.startswith('Rotor3:'):
                code_info.append(line[line.find('[') + 1: line.find(']')])
                break
        return code_info



#making the code of a special date and encipher it
def get_code(date ,code):

    #making maps

    key_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    date_info = Files()
    date_info_list = date_info.getData(date)


    plugboard = MyMap()
    plugboard.hash_function(key_list, date_info_list[0])

    rotor1 = MyMap()
    rotor1.hash_function(key_list, date_info_list[1])

    rotor2 = MyMap()
    rotor2.hash_function(key_list, date_info_list[2])

    rotor3 = MyMap()
    rotor3.hash_function(key_list, date_info_list[3])

    reflector = MyMap()
    reflector.hash_function(key_list, key_list[::-1])


    #initializing the code class

    code_class = Code(date, rotor1, rotor2, rotor3, plugboard, reflector)

    deciphered_code = decipher(code ,code_class)


    return deciphered_code


def decipher(text_code, code_class):

    rotor1_rotation = 0
    rotor2_rotation = 0
    rotor3_rotation = 0

    return null

