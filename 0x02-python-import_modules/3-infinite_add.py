#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sum = 0
    for num in sys.argv[1:]:
        sum += int(num)
    print(sum)
