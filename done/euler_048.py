#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Self powers
Problem 48
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""


def power_series(number):
    series_sum = 0
    for i in range(1, number + 1):
        series_sum += i ** i
    return series_sum


series_sum_1000 = power_series(1000) % 10000000000
print("Answer: {}".format(series_sum_1000))
