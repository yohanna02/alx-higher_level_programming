#!/usr/bin/python3
def remove_char_at(str, n):
    index = 0
    new_string = ""
    for i in str:
        if (index == n):
            index += 1
            continue
        new_string += i
        index += 1
    return new_string
