# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler

import math

cash = {}


def divList(x):
    leeest = []
    for i in range(1, int(x / 2) + 1):
        if x % i == 0:
            leeest.append(i)
    return leeest


def numDivs(x):
    n = 0
    for i in range(int((1 + x) / 2), 0, -1):
        # print(i)
        if x % i == 0:
            n += 1
    return n


curTriangleNum = 1
maxDivs = 1
notDoneYet = True
# for i in range(10):
i = 1
while(notDoneYet):
    i += 1
    curTriangleNum = curTriangleNum + i
    if
    listODivs = divList(curTriangleNum)
    # lengthList = numDivs(curTriangleNum)

    if (maxDivs < lengthList):
        maxDivs = lengthList
        print("\n***")
        print("NEW MAX")
        print("index: {}".format(i))
        print("cur: {}".format(curTriangleNum))
        # print("divs: {}".format((listODivs)))
        # print("lenlist: {}".format(len(listODivs)))
        print("# div: {}".format(lengthList))

        if(maxDivs > 500):
            notDoneYet = False

    # if (numbDivs % 100 == 0):
    #     print("\n***")
    #     print("index: {}".format(i))
    #     print("cur: {}".format(curTriangleNum))
    #     print("divs: {}".format(numbDivs))
    #     print("# div: {}".format(numbDivs))

#!/usr/bin/env python
# Jesse Rubin - project Euler

# Highly divisible triangular number
# Problem 12
# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?

import math
from functools import lru_cache


@lru_cache(maxsize=None)
def divisors(n):
    large_divisors = []
    divs = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            divs.append(i)
            if i * i != n:
                large_divisors.append(n // i)
    return set(divs + large_divisors)


@lru_cache(maxsize=None)
def nDivisors(n):
    divs = []
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            divs.append(i)
            if i * i != n:
                divs.append(n // i)
    return len(set(divs + large_divisors))


cur_triangle_number = 0
maxmax = 1
for i in range(1, 20):
    cur_triangle_number += i
    numDivs = nDivisors(cur_triangle_number)
    if (numDivs > maxmax):
        maxmax = numDivs
        print("***")
        print("NEW MAX")
        print("index: {}".format(i))
        print("cur #: {}".format(cur_triangle_number))
        print(nDivisors(cur_triangle_number))
