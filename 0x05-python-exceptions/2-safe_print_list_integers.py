#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in my_list:
        try:
            if count == x:
                break
            print("{:d}".format(i), end="")
            if count < x - 1:
                print("", end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count
