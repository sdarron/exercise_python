#! /usr/bin/python3

import sys

while True:
    print('Type exit to exit.')
    respons = input()
    if respons == 'exit':
        sys.exit()
    print('You tiped ' + respons + '.')
