#!/usr/bin/python

import sys
import bisect
from itertools import izip as zip, count # izip for maximum efficiency

#Locate the leftmost value exactly equal to x
def index(a, x):
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

# Sort prices, discarding every price lower than credit
# It finishes when the first solution comes up
def solve(credit, items, prices):
    indexes = prices.split(' ')
    ps = sorted(map(int, prices.split(' ')))
    r_idx = bisect.bisect_left(ps, credit)
    ps = ps[0:r_idx]
    while True:
        if len(ps) == 1:
            break
        # Choose a number (any will do) and slice it out
        first = ps.pop()
        diff = abs(first - credit)
        # Try to find complement, if it exists, break
        # If not: remove, try again with the remaining items
        try:
            second_idx = index(ps, diff)
            second = ps[second_idx]
            break
        except ValueError:
            pass

    idxs_search = [i for i, j in zip(count(), indexes) if j == str(first)]
    if len(idxs_search) == 1:
        first_idx = idxs_search[0]
        second_idx = indexes.index(str(second))
        if(first_idx > second_idx):
            tmp = first_idx
            first_idx = second_idx
            second_idx = tmp   
    else:
        first_idx = idxs_search[0]
        second_idx = idxs_search[1]
 
    return [first_idx + 1, second_idx + 1]

input = open(sys.argv[1])
cases = int(input.readline())
for case in range(1, cases+1):
    # read three lines which will be used to solve one case
    credit = int(input.readline().rstrip('\n'))
    items = int(input.readline().rstrip('\n'))
    prices = input.readline().rstrip('\n')
    idxs = solve(credit, items, prices)
    print "Case #{}: {} {}".format(case, idxs[0], idxs[1])
input.close()

