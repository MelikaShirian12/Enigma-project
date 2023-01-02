import serial
import time

# ArduinoSerial = serial.Serial('com8', 9600)
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
def MyRotate(l, n):
    return l[n:] + l[:n]
class Code:
    # def __int__(self, date, rotor1, rotor2, rotor3, plugboard, reflector):
    #     self.date = date
    #     self.rotor1 = rotor1
    #     self.rotor2 = rotor2
    #     self.rotor3 = rotor3
    #     self.plugboard = plugboard
    #     self.reflector = reflector

    def setData(self ,date, rotor1, rotor2, rotor3, plugboard, reflector):
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
        self.table = list()

        self.keyCharacters = list(keyCharacters)
        self.valueCharacters = list(valueCharacters)

        for i in range(len(keyCharacters)):
            new_entry = Entry(keyCharacters[i], valueCharacters[i])
            self.table.append(new_entry)

        return self.table

    def rotation(self):

        self.valueCharacters = MyRotate(self.valueCharacters , -1)

        self.hash_function(self.keyCharacters ,self.valueCharacters)


    def find_value(self , value):

        for entry in self.table:
            if entry.value == value:
                return entry

    def find_key(self, key):

        for entry in self.table:
            if entry.key == key:
                return entry


class Entry:

    def __init__(self, key, value):
        self.key = key
        self.value = value
class Files:

# Kianoosh's ---> D:\\Private\\uni\\Coding\\DS_ENIGMA_MACHINE\\Enigma-project\\Enigma-project\\Files\\EnigmaFile.txt
# Melika's --->  D:\\university\\programs-data struct\\github projects\\enigma pro\\Enigma-project\\Files\\EnigmaFile.txt
    def getData(self, date):
        code_info = list()
        check = False

        file = open('D:\\Private\\uni\\Coding\\DS_ENIGMA_MACHINE\\Enigma-project\\Enigma-project\\Files\\EnigmaFile.txt')
        for line in file:
            if line.startswith('Date: ' + date):
                check = True
                continue
            if check and line.startswith('PlugBoard:'):
                code_info.append(line[line.find('[') + 1: line.find(']')])
                code_info[len(code_info) - 1] = str(code_info[len(code_info) - 1]).upper()
            elif check and line.startswith('Rotor1:'):
                code_info.append(line[line.find('[') + 1: line.find(']')])
                code_info[len(code_info) - 1] = str(code_info[len(code_info) - 1]).upper()
            elif check and line.startswith('Rotor2:'):
                code_info.append(line[line.find('[') + 1: line.find(']')])
                code_info[len(code_info) - 1] = str(code_info[len(code_info) - 1]).upper()
            elif check and line.startswith('Rotor3:'):
                code_info.append(line[line.find('[') + 1: line.find(']')])
                code_info[len(code_info) - 1] = str(code_info[len(code_info) - 1]).upper()
                break
        return code_info



def make_plug_board_value(code, plugboard):
    plugboard = str(plugboard).upper()
    tmp_list = list()
    for i in plugboard:
        if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
            tmp_list.append(i)
    code = list(code)
    for j in range(len(code)):
        for i in range(0, len(tmp_list), 2):
            if code[j] == tmp_list[i]:
                code[j] = tmp_list[i + 1]
            elif code[j] == tmp_list[i + 1]:
                code[j] = tmp_list[i]
                break
    return ''.join(code)


# making the code of a special date and encipher it
def get_code(date, code):
    # making maps

    key_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #'DG, BF, MU, JC, KA, SY, HL, OX'
    date_info = Files()
    date_info_list = date_info.getData(date)


    plugboard = MyMap()
    tmp = make_plug_board_value(key_list, date_info_list[0])
    plugboard.hash_function(key_list, tmp)

    rotor1 = MyMap()
    rotor1.hash_function(key_list, date_info_list[1])

    rotor2 = MyMap()
    rotor2.hash_function(key_list, date_info_list[2])

    rotor3 = MyMap()
    rotor3.hash_function(key_list, date_info_list[3])

    reflector = MyMap()
    reflector.hash_function(key_list, key_list[::-1])

    # initializing the code class

    # code_class = Code(date, rotor1, rotor2, rotor3, plugboard, reflector)
    code_class = Code()
    code_class.setData(date, rotor1, rotor2, rotor3, plugboard, reflector)

    deciphered_code = decipher(code, code_class)


    return deciphered_code


def decipher(text_code, code_class):

    rotor1_rotation = 0
    rotor2_rotation = 0
    rotor3_rotation = 0

    new_text = list()

    for i in range(len(text_code)):
        #'DG, BF, MU, JC, KA, SY, HL, OX'
        #before reflection:
        #these should be value because they are the keys of the next reflector
        entry = code_class.plugboard.find_key(text_code[i])
        entry = code_class.rotor3.find_key(entry.value)
        entry = code_class.rotor2.find_key(entry.value)
        entry = code_class.rotor1.find_key(entry.value)

        #after reflection

        entry = code_class.reflector.find_key(entry.value)

        entry = code_class.rotor1.find_value(entry.value)
        entry = code_class.rotor2.find_value(entry.key)
        entry = code_class.rotor3.find_value(entry.key)

        entry = code_class.plugboard.find_value(entry.key)


        new_text.append(entry.key)

        code_class.rotor3.rotation()
        rotor3_rotation += 1
        if rotor3_rotation == 26:
            rotor3_rotation = 0
            code_class.rotor2.rotation()
            rotor2_rotation += 1
            if rotor2_rotation == 26:
                rotor2_rotation = 0
                code_class.rotor1.rotation()




    return new_text


#Main :
date = str()
data = str()
date_check = bool(False)
data_check = bool(False)
ArduinoSerial = serial.Serial('com8',9600)
time.sleep(2)
print(ArduinoSerial.readline())
read = ArduinoSerial.readline()
while True:
    if str(read).find(':') != -1:
        print(str(read)[str(read).find(':') + 1 : str(read).index('\\')]) #is the sent value from Mobile
        tmp = str(read)[str(read).find(':') + 1 : str(read).index('\\')]
        if tmp.find('/') != -1:
            date = tmp
            date_check = True
        else:
            data = tmp
            data_check = True

    if date_check and data_check:

        data = str(data).upper()
        deciohered_code = get_code(date , data)
        print(''.join(deciohered_code).lower())


        data_check = False
        date_check = False
        data = None
        date = None
    read = ArduinoSerial.readline()

