#!/usr/bin/python3
for i in range(90, 64, -1):
    character = chr(i)
    if i % 2 == 0:
        character = character.lower()
    print("{}".format(character), end="")
