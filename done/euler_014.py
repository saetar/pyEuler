#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin
"""
Longest Collatz sequence
Problem 14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

from functools import lru_cache
from operator import itemgetter

@lru_cache(maxsize=None)
def collatz_seq_length(n):
    if (n == 1): return 1
    if n%2==0: return collatz_seq_length(n//2) + 1
    else: return collatz_seq_length(3*n + 1) + 1

seq_lengths = [collatz_seq_length(i) for i in range(1, 1000000)]

max_index, sequence_length = max(enumerate(seq_lengths), key=itemgetter(1))
print("{} produces a collatz sequence length of {}".format(max_index, sequence_length))
print("THIS IS THE ANSWER!!!")
