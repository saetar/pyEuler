#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN - Biblioteca
from bisect import bisect_right, bisect_left
from itertools import count, chain
from math import log

from bib import xrange
from bib.maths import divisors_gen
from bib.decorations import cash_it


def prime_gen(plim=0, kprimes=None):
    """
    infinite (within reason) prime number generator

    My big modification is the pdiv_dictionary() function that recreats the
    dictionary of divisors so that you can continue to generate prime numbers
    from a (sorted) list of prime numbers.

    BASED ON:
        eratosthenes by David Eppstein, UC Irvine, 28 Feb 2002
        http://code.activestate.com/recipes/117119/
        and
        the thread at that url


    :param plim: upper limit of numbers to check
    :param kprimes: known primes list
    :return:
    """

    if kprimes is None: kprimes = [2, 3, 5, 7, 11]

    def _pdiv_dictionary():
        """
        Recreates the prime divisors dictionary used by the generator
        """
        div_dict = {}
        for pdiv in kprimes:  # for each prime
            multiple = kprimes[-1] // pdiv * pdiv
            if multiple % 2 == 0:
                multiple += pdiv
            else:
                multiple += 2 * pdiv
            while multiple in div_dict:
                multiple += pdiv * 2
            div_dict[multiple] = pdiv
        return div_dict

    # [1]
    # See if the upper bound is greater than the known primes
    if 0 < plim <= kprimes[-1]:
        for p in kprimes:
            if p <= plim:
                yield p
        return  # return bc we are done

    # [2]
    # Recreate the prime divisibility dictionary using kprimes;
    # Set start and yield first 4 primes
    divz = _pdiv_dictionary()
    start = kprimes[-1] + 2  # max prime + 2 (make sure it is odd)
    if start == 13:
        yield 2
        yield 3
        yield 5
        yield 7
        yield 11
    # use count or range depending on if generator is infinite
    it = count(start, 2) if plim == 0 else xrange(start, plim, 2)

    for num in it:
        prime_div = divz.pop(num, None)
        if prime_div:
            multiple = (2 * prime_div) + num
            while multiple in divz:
                multiple += (2 * prime_div)
            divz[multiple] = prime_div
        else:
            divz[num * num] = num
            yield num


def pfactorization_gen(n):
    """

    Args:
        n:

    Returns:

    """
    return (n for n in chain.from_iterable([p] * int(log(n, p))
                                           for p in pfactors_gen(n)))


def pfactors_gen(n):
    """
    Returns prime factorization as a list

    :param n:
    :return:
    """
    return (p for p in divisors_gen(n) if is_prime(p))


@cash_it
def is_prime(number):
    """
    Returns True if number is prime

    >>> is_prime(37)
    True
    >>> is_prime(100)
    False
    >>> is_prime(89)
    True
    """
    if number == 2 or number == 3:
        return True
    if number < 2 or number % 2 == 0:
        return False
    if number < 9:
        return True
    if number % 3 == 0:
        return False
    r = int(number**0.5)
    step = 5
    while step <= r:
        if number % step == 0:
            return False
        if number % (step + 2) == 0:
            return False
        step += 6
    return True


class OctopusPrime(list):
    """
    OctopusPrime, the 8-leg autobot, here to help you find PRIMES

    ______OCTOPUS_PRIME ACTIVATE______
    ░░░░░░░▄▄▄▄█████████████▄▄▄░░░░░░░
    ████▄▀████████▀▀▀▀▀▀████████▀▄████
    ▀████░▀██████▄▄░░░░▄▄██████▀░████▀
    ░███▀▀█▄▄░▀▀██████████▀▀░▄▄█▀▀███░
    ░████▄▄▄▀▀█▄░░░▀▀▀▀░░░▄█▀▀▄▄▄████░
    ░░██▄▄░▀▀████░██▄▄██░████▀▀░▄▄██░░
    ░░░▀████▄▄▄██░██████░██▄▄▄████▀░░░
    ░░██▄▀▀▀▀▀▀▀▀░░████░░▀▀▀▀▀▀▀▀▄██░░
    ░░░██░░░░░░░░░░████░░░░░░░░░░██░░░
    ░░░███▄▄░░░░▄█░████░█▄░░░░▄▄███░░░
    ░░░███████░███░████░███░███████░░░
    ░░░███████░███░▀▀▀▀░███░███████░░░
    ░░░███████░████████████░███████░░░
    ░░░░▀█████░███░▄▄▄▄░███░█████▀░░░░
    ░░░░░░░░▀▀░██▀▄████▄░██░▀▀░░░░░░░░
    ░░░░░░░░░░░░▀░██████░▀░░░░░░░░░░░░
    """

    def __init__(self, n=10, savings_n_loads=True, save_path=None):
        list.__init__(self, list(prime_gen(plim=n)))
        self.max_loaded = self[-1]

    def transform(self, n=None):
        """

        Args:
            n:
        """
        n = n if n is not None else self[-1] * 10
        self.extend(list(prime_gen(plim=n, kprimes=self)))

    def is_prime(self, number):
        """Ask Octopus Prime if a number is prime

        Args:
            number: the number you are inquiring about

        Returns:
            Bool: True if the number is prime and False otherwise

        """
        if number > self[-1]:
            self.transform(number + 1)
        if number in self:
            return True
        else:
            return False

    def primes_below(self, upper_bound):
        """

        Args:
            upper_bound:

        Returns:

        """
        return self.primes_between(1, upper_bound)

    def primes_between(self, lower_bound, upper_bound):
        """

        Args:
            lower_bound:
            upper_bound:

        Returns:

        """
        if upper_bound > self[-1]:
            self.transform(upper_bound)
        return self[bisect_right(self, lower_bound):bisect_left(
            self, upper_bound)]
