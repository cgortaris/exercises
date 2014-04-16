#!/usr/bin/python

import sys

input = open(sys.argv[1])
cases = int(input.readline())
for case in range(1, cases + 1):
    line = input.readline().rstrip('\n')
    # Store all words in a LIFO list
    lifo = []
    word = ''
    for i in range(0, len(line)):
        if line[i] == ' ':
            lifo.insert(0, word)
            word = ''
        else:
            word += line[i]
    lifo.insert(0, word)
    print "Case #{}: {}".format(case, ' '.join(lifo))
input.close()

