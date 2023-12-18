#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        while True:
            item = my_list[count]
            print(item, end='')
            count += 1
            if count == x:
                break
        print()
        return count
    except IndexError:
        print()
        return count
