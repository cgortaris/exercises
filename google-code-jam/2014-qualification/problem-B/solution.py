#!/usr/bin/python

import sys

# Calculates a strategy's time upon buying n farms
def stgtime(n, rate, C, F, X):
    time = 0
    for buy in range(1, n + 1):
        time += C / rate
        rate += F
    time += X / rate
    return time

input = open(sys.argv[1])
cases = int(input.readline())
rate = 2
# To find the best strategy we compare time taken when increasing number of farms are bought, doubling the number and then performing binary search of the optimal number of farms
for case in range(1, cases + 1):
    [C, F, X] = map(float, input.readline().rstrip().split(' '))
    step = 1
    lb = 0
    lt = stgtime(lb, rate, C, F, X)
    bt = lt
    rb = 1
    rt = stgtime(rb, rate, C, F, X)
    while True:
        # Check trend of right pivot
        pb = rb - 1
        pt = stgtime(pb, rate, C, F, X)
        nb = rb + 1
        nt = stgtime(nb, rate, C, F, X)
        if nt < rt: # keep going down
            lb = nb
            lt = nt
            rb = nb + step
            rt = stgtime(rb, rate, C, F, X)
            step *= 2
        elif pt < rt: # trend change => binary search between [lt, rt]
            rb = pb
            rt = pt
            while True:
                mb = int((rb + lb) / 2)
                mt = stgtime(mb, rate, C, F, X)
                pb = mb - 1
                pt = stgtime(pb, rate, C, F, X)
                nb = mb + 1
                nt = stgtime(nb, rate, C, F, X)
                if pt < mt:
                    rb = pb
                    rt = pt
                elif nt < mt:
                    lb = nb
                    lt = nt
                else:
                    bt = mt
                    break
        else: # rt is the optimal
            bt = rt
            break
    print "Case #{}: {}".format(case, bt)
input.close()
