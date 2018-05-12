#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN - Biblioteca
"""
My (Jesse Rubin) library of functions/methods and classes that I use on the reg
"""
from __future__ import absolute_import, division, generators, print_function

from math import acos, pi, sqrt
from operator import add, floordiv, methodcaller, sub, truediv

from lib.decorations import cash_it

try: xrange
except NameError: xrange = range


##############
# GENERATORS #
##############


# DECORATORS #

# CLASSES #


def partitions_gen(max_p, min_p=1):
    """Partitions generator

    Args:
        max_p (int): number for which to yield partiton tuples
        min_p (int): smallest partition size

    Yields:
        tuple: partition of max_p with smallest partition being min_p
    """
    yield (max_p,)
    for i in xrange(min_p, max_p//2+1):
        for p in partitions_gen(max_p-i, i):
            yield (i,)+p


@cash_it
def rfactorial(n):
    """Recursive factorial function

    Args:
        n:

    Returns:

    """
    if n == 1:
        return 1
    else:
        return rfactorial(n-1)*n


def radians_2_degrees(rads):
    """Converts radians to degrees"""
    return 180*rads/pi


def degrees_2_radians(degs):
    """Converts degrees to radians"""
    return degs*pi/180


def power_mod(number, exponent, mod):
    """

    Args:
        number:
        exponent:
        mod:

    Returns:

    """
    if exponent > 0:
        if exponent%2 == 0:
            return power_mod(number, floordiv(exponent, 2), mod)
        else:
            return power_mod(number, floordiv(exponent, 2), mod)*number
    else:
        return 1


def divisors_gen(n):
    """Divisors generator

    Args:
        n (int): number w/ divisors to be generated

    Yields:
        int: divisors

    """
    large_divisors = []
    for i in xrange(1, int(sqrt(n)+1)):
        if n%i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n//i)
    for divisor in reversed(large_divisors):
        yield divisor


def gcd_it(a, b):
    """iterative gcd"""
    while a:
        a, b = b%a, a
    return b


@cash_it
def gcd_r(a, b):
    """recursive greatest common divisor"""
    if b > a:
        return gcd_r(b, a)
    r = a%b
    if r == 0:
        return b
    return gcd_r(r, b)


def reverse(n):
    """Reverses a number

    Args:
        n (int): number to be reversed

    Returns:
        int: reversed of a number

    """

    reversed = 0
    while n > 0:
        reversed *= 10
        reversed += n%10
        n //= 10
    return reversed


@cash_it
def fib_r(n):
    """Recursively the nth fibonacci number

    Args:
        n (int): nth fibonacci sequence number

    Returns:
        int: the nth fibonacci number

    Examples:
        >>> fib_r(1)
        1
        >>> fib_r(2)
        2
        >>> fib_r(6)
        13
    """
    return n if n < 3 else fib_r(n-1)+fib_r(n-2)


def expo(d, n):
    """greatest exponent for a divisor of n

    Args:
        d (int): divisor
        n (int): number be divided

    Returns:
        int: number of times a divisor divides n
    """
    if n < d:  # flip
        d, n = n, d
    c = n
    divs = 0
    while c%d == 0:
        c //= d
        divs += 1
    return divs


def pytriple_gen(max_c):
    """primative pythagorean triples generator

    special thanks to 3Blue1Brown's video on pythagorean triples
    https://www.youtube.com/watch?v=QJYmyhnaaek&t=300s

    Args:
        max_c (int): max value of c to yeild triples up to

    Yields:
        tuple: pythagorean triple (a, b, c)
    """
    for real_pts in xrange(2, int(sqrt(max_c))+1, 1):
        for imag_pts in xrange(real_pts%2+1, real_pts, 2):
            comp = complex(real_pts, imag_pts)
            sqrd = comp*comp
            real = int(sqrd.real)
            imag = int(sqrd.imag)
            if abs(real-imag)%2 == 1 and gcd_it(imag, real) == 1:
                sea = int((comp*comp.conjugate()).real)
                if sea > max_c:
                    break
                else:
                    yield (imag, real, sea) if real > imag else (real, imag, sea)


class Trigon(object):
    """
    Trigon object composed of three points connected by lines.
    """

    def __init__(self, pt1, pt2, pt3):
        self.pt1 = Vuple(pt1)
        self.pt2 = Vuple(pt2)
        self.pt3 = Vuple(pt3)

    @classmethod
    def from_points(cls, pts):
        """

        Args:
            pts:

        Returns:

        """
        if len(pts) == 3:
            return Trigon(*pts)
        if len(pts) == 6:
            it = iter(pts)
            return Trigon(*zip(it, it))

    def __str__(self):
        return "<< {}, {}, {} >>".format(self.pt1, self.pt2, self.pt3)

    def __contains__(self, point):
        if type(point) is not Vuple:
            point = Vuple(point)
        return self.area() == sum(map(methodcaller('area'),
                                      self.inner_triangles(point)))

    def inner_triangles(self, point):
        """Triangle funk that returns the three triangles w/ a point

        The point (p) is connected to each point of a triangle. with points,
        a, b, and c. The three triangles are t1=(a, b, p), t2=(a, c, p), and
        t3 = (b, c, p).

        Args:
            point (tuple or Vuple): point to connect to Triangle Vertices

        Returns:
            t1, t2, t3 (Trigon): Three triangles

        """
        t1 = Trigon(point, self.pt2, self.pt3)
        t2 = Trigon(self.pt1, point, self.pt3)
        t3 = Trigon(self.pt1, self.pt2, point)
        return t1, t2, t3

    def is_perimeter_point(self, point):
        """

        Args:
            point:

        Returns:

        """
        if type(point) is not Vuple:
            point = Vuple(point)
        return any(tri_area == 0 for tri_area in
                   map(methodcaller('area'), self.inner_triangles(point)))

    def points(self):
        """

        Returns:

        """
        return self.pt1, self.pt2, self.pt3

    def contains_origin(self):
        """True if the origin (0,0) lies within the Triangle

        Returns:

        """
        return (0, 0) in self

    def area(self):
        """

        Returns:

        """
        return abs(truediv(Vuple.cproduct(self.pt1-self.pt2,
                                          self.pt3-self.pt2), 2))

    @staticmethod
    def area_from_points(pt1, pt2, pt3):
        """

        Args:
            pt1:
            pt2:
            pt3:

        Returns:

        """
        return abs(truediv(Vuple.cproduct(pt1-pt2, pt3-pt2), 2))


class Vuple(tuple):
    """
    Vector-Tuple class
    """

    def __gt__(self, other):
        """Greater than based on magnitude (proportional)

        :param other:
        :return:
        """
        return Vuple.mag_sqrd(self) > Vuple.mag_sqrd(other)

    def __eq__(self, other):
        return Vuple.mag_sqrd(self) == Vuple.mag_sqrd(other)

    def __add__(self, other):
        return Vuple(map(add, self, other))

    def __sub__(self, other):
        return Vuple(map(sub, self, other))

    def __mul__(self, k):
        if type(k) is int or type(k) is float:
            return self._mul_scalar(k)
        # return Vuple(map(sub, self, k))

    def __imul__(self, k):
        if type(k) is int or type(k) is float:
            return self._mul_scalar(k)

    def _mul_scalar(self, k):
        return Vuple((k*el for el in self))

    def __truediv__(self, k):
        if type(k) is int or type(k) is float:
            return self._truediv_scalar(k)
        # return Vuple(map(sub, self, k))

    def __itruediv__(self, k):
        if type(k) is int or type(k) is float:
            return self._truediv_scalar(k)

    def _truediv_scalar(self, k):
        return Vuple((el/k for el in self))

    def normalize(self):
        """

        Returns:

        """
        return Vuple.unit_vuple(self)

    @staticmethod
    def unit_vuple(voop):
        """

        Args:
            voop:

        Returns:

        """
        return Vuple(voop)/Vuple.mag(voop)

    def get_mag_sqrd(self):
        """

        Returns:

        """
        return Vuple.mag_sqrd(self)

    @staticmethod
    def mag_sqrd(voop):
        """

        Args:
            voop:

        Returns:

        """
        return sum(el*el for el in voop)

    def get_mag(self):
        """

        Returns:

        """
        return Vuple.mag(self)

    @staticmethod
    def mag(voop):
        """

        Args:
            voop:

        Returns:

        """
        return sqrt(Vuple.mag_sqrd(voop))

    @staticmethod
    def dproduct(a, b):
        """

        Args:
            a:
            b:

        Returns:

        """
        return sum(va*vb for va, vb in zip(a, b))

    @staticmethod
    def cproduct(v1, v2):
        """Cross product of two 2d vectors

        :param v1: first vector
        :param v2: second vector
        :return: cproduct product
        """
        if len(v1) == 2 and len(v2) == 2:
            return (v1[0]*v2[1])-(v1[1]*v2[0])

    @staticmethod
    def angle(v1, v2, radians=True):
        """

        Args:
            v1:
            v2:
            radians:

        Returns:

        """
        # return acos(Vuple.dproduct(v1, v2)/(Vuple.mag(v1)*Vuple.mag(v2)))
        q = 1 if radians else 180/pi
        return q*acos(Vuple.dproduct(Vuple.unit_vuple(v1),
                                     Vuple.unit_vuple(v2)))


def is_palindrome(string):
    """True a string is a palindrome.

    Doctests:
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("greg")
    False
    """
    for index, character in enumerate(string):
        if character != string[-index-1]:
            return False
    return True


if __name__ == '__main__':
    import doctest

    doctest.testmod()