#!/usr/bin/python3

# defining a function that reads a text file (UTF8) and prints it to stdout
def read_file(filename=""):
    # scripting the function that reads the txt file
    with open(filename, encoding="utf-8") as fi:
        print(fi.read(), end="")
