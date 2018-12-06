#!/usr/bin/env python3

import os
import sys

def hr(char, cols):
    line = ''
    while len(line) < cols:
        line += char

    # Clip some off in case cols isn't a multiple of length of char
    print(line[:cols]) 

def main():
    rows, columns = os.popen('stty size', 'r').read().split()

    if len(sys.argv) > 1:
        chars = sys.argv[1:]
    else:
        chars = ['#']


    for value in chars:
        hr(value, int(columns))



if __name__ == '__main__':
    main()
