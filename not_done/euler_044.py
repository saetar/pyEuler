#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler

"""
Pentagon numbers
Problem 44
Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten
pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference,
70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and
difference are pentagonal and D = |Pk − Pj| is minimised; what is the value
of D?
"""

from functools import lru_cache


@lru_cache(maxsize=None)
def pent_num(n):
    return n * (3 * n - 1) // 2

pen_nums = set()
for i in range(100):
    for j in range(i):
        print("___")
        pen_nums.add(pent_num(i))
        sum = pent_num(i) + pent_num(j)
        diff = pent_num(i) - pent_num(j)
        if sum in pen_nums and diff in pen_nums:

            print(i)
            print(j)
            print(sum)
            print(diff)

# pentagonal_nums = []
# for i in range(1, 10):
# i = 0
# while(True):
#     pni = pent_num(i)
#     for num in pentagonal_nums:
#         # print("___")
#         # print(pent_num(i))
#         sub_diff = abs(num - pni)
#         add_diff = num + pni
#         if sub_diff in pentagonal_nums and add_diff in pentagonal_nums:
#             print(sub_diff)
#             print(add_diff)
#             break
#     pentagonal_nums.append(pni)
#     i += 1
