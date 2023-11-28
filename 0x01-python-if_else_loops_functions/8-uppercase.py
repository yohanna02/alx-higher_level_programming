#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for i in str:
        unicode = ord(i)
        if unicode >= 97 and unicode <= 122:
            new_str += chr(unicode - 32)
        else:
            new_str += i
    print("{}".format(new_str))
