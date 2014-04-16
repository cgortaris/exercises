#!/usr/bin/python

import sys

def solve(first, second):
    contains = 0
    for guess in first:
        if guess in second:
            contains += 1
            match = guess
    if contains == 0:
        answer = 'Volunteer cheated!'
    elif contains == 1:
        answer = match
    elif contains > 1:
        answer = 'Bad magician!'
    return answer

input = open(sys.argv[1])
cases = int(input.readline())
for case in range(1, cases + 1):
    first_row = int(input.readline())
    rows = {
        'first': [],
        'second': []
    }
    rows['first'] = []
    for i in range(0, 4):
        rows['first'].append(set(input.readline().rstrip('\n').split(' '))) # search on sets are O(1)
    second_row = int(input.readline())
    for i in range(0, 4):
        rows['second'].append(set(input.readline().rstrip('\n').split(' ')))
    answer = solve(rows['first'][first_row - 1], rows['second'][second_row - 1])
    print "Case #{}: {}".format(case, answer)
input.close()

