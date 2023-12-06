#!/usr/bin/python3
def uniq_add(my_list=[]):
    used = []
    sum = 0
    for list_item in my_list:
        if list_item in used:
            continue
        used.append(list_item)
        sum += list_item
    return sum
