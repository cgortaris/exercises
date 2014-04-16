#!/usr/bin/python

import sys

key_presses = {
    'a': '2',
    'b': '22',
    'c': '222',
    'd': '3',
    'e': '33',
    'f': '333',
    'g': '4',
    'h': '44',
    'i': '444',
    'j': '5',
    'k': '55',
    'l': '555',
    'm': '6',
    'n': '66',
    'o': '666',
    'p': '7',
    'q': '77',
    'r': '777',
    's': '7777',
    't': '8',
    'u': '88',
    'v': '888',
    'w': '9',
    'x': '99',
    'y': '999',
    'z': '9999',
    ' ': '0'
}

input = open(sys.argv[1])
cases = int(input.readline())
for case in range(1, cases + 1):
    line = input.readline().rstrip('\n')
    # We just replace every letter with key presses needed
    translation = ''
    for i in range(0, len(line) - 1):
        translation += key_presses[line[i]]
        if key_presses[line[i]][0] == key_presses[line[i + 1]][0]:
            translation += ' '
    translation += key_presses[line[len(line) - 1]]
    print "Case #{}: {}".format(case, translation)
input.close()

