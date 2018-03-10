#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Powerful digit counts
Problem 63
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit
number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""
from itertools import count
from lib.decorations import tictoc

def powerful_digits(n):
    max_n_digit_num = (10**n)-1
    current = 0
    n_powerful_digits = 0
    for i in count(1):
        current = i ** n
        if current >= 10**(n-1) and current < 10**n:
            n_powerful_digits += 1
        elif current > max_n_digit_num:
            return n_powerful_digits

@tictoc
def number_of_powerful_digits():
    total_powerful_digits = 0
    for ndigs in count(1):
        result = powerful_digits(ndigs)
        total_powerful_digits += result
        if result == 0:
            return total_powerful_digits

answer = number_of_powerful_digits()
print("Total number of powerful digits: {}".format(answer))