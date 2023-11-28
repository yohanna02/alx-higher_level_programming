#!/usr/bin/python3
for i in range(0, 100):
    print("{0}".format("0"+str(i) if i < 10 else i), end="")
    print("{0}".format("\n" if i == 99 else ", "), end="")
