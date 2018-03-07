# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Jesse Rubin - project Euler
# JESSE'S pEuler helper functions

from math import sqrt
from collections import deque
from functools import lru_cache


@lru_cache(maxsize=None)
def is_prime(number: int) -> bool:
    """
    Returns True if number is prime

    >>> is_prime(37)
    True
    >>> is_prime(100)
    False
    >>> is_prime(89)
    True
    """
    if number % 2 == 0 and number > 2: return False
    else: return all(number % i for i in range(3, int(sqrt(number) + 1), 2))

@lru_cache(maxsize=None)
def cash_factorial(n):
    if n == 1:
        return 1
    else:
        return cash_factorial(n-1) * n

def prime_factorization(n):
    """
    Returns prime factorization as a list

    :param n:
    :return:
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


@lru_cache(maxsize=None)
def is_perfect_square(positive_n):
    if positive_n < 5:
        if positive_n == 4 or positive_n == 1:
            return True
        return False
    half = positive_n // 2
    seen_set = {half}
    while half * half != positive_n:
        half = (half + (positive_n // half)) // 2
        if half in seen_set:
            return False
        seen_set.add(half)
    return True


@lru_cache(maxsize=None)
def fib(n: int) -> int:
    """Return the nth fibonacci number

    :param n: nth fib number index
    :return: nth fib number

    >>> fib(1)
    1
    >>> fib(2)
    2
    >>> fib(6)
    13
    """
    if n < 3:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


@lru_cache(maxsize=None)
def is_circ_prime(n):
    digist = [int(j) for j in digits_list(n)]
    return all(
        (is_prime(dig_list_2_int(i)) for i in number_rotations_generator(digist)))


@lru_cache(maxsize=4)
def divisors_gen(n):
    large_divisors = []
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n // i)
    for divisor in reversed(large_divisors):
        yield divisor


@lru_cache(maxsize=None)
def n_divisors(n):
    """
    >>> n_divisors(12)
    6
    >>> n_divisors(10)
    4
    """
    return sum(1 for _ in divisors_gen(n))


def divisors_list(n):
    return [i for i in divisors_gen(n)]


def number_rotations_generator(l):
    for i in range(len(l)):
        yield (l[-i:] + l[:-i])


def is_palindrome(string):
    """True a string is a palindrome.

    Doctests:
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("greg")
    False
    """
    for index, character in enumerate(string):
        if character != string[-index - 1]:
            return False
    return True


def int_to_binary_string(n):
    return bin(n)[2:]


def rotate_list(l, n):
    return l[-n:] + l[:-n]


def num_base_ten_digits(number: int) -> int:
    return sum((1 for _ in str(number)))


def digits_list(num):
    """Returns a list of the digits in a number

    >>> digits_list(1111)
    [1, 1, 1, 1]
    >>> digits_list(982)
    [9, 8, 2]
    >>> digits_list(101)
    [1, 0, 1]
    >>> digits_list(123)
    [1, 2, 3]
    """
    digits = deque()
    while True:
        num, r = divmod(num, 10)
        digits.appendleft(r)
        if num == 0:
            break
    return list(digits)


def cross_prod_2d(v1: tuple or list, v2: tuple or list) -> int:
    """Cross product of two 2d vectors

    :param v1: first vector
    :param v2: second vector
    :return: cross product
    """
    return (v1[0] * v2[1]) - (v1[1] * v2[0])


def dig_list_2_int(l):
    """
    >>> dig_list_2_int([3, 2, 1])
    321
    >>> dig_list_2_int([1, 1, 1, 1, 2, 3])
    111123
    >>> dig_list_2_int([1, 2, 3])
    123
    """
    d = 0
    n_digs = len(l)
    for i in range(0, n_digs, 1):
        d += (l[n_digs - i - 1] * 10 ** i)
    return d


def string_score(name):
    """
    >>> string_score('me')
    18
    >>> string_score('poooood')
    95
    >>> string_score('gregory')
    95
    """
    return sum((ord(character) - 96 for character in name.lower()))


if __name__ == '__main__':
    import doctest
    doctest.testmod()  # run doctests if this script is called
