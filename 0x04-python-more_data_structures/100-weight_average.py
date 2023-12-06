#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum = 0
    divide_by = 0
    for item in my_list:
        sum += item[0] * item[1]
        divide_by += item[1]
    return sum / divide_by
