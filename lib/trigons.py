#!/usr/bin/env python
# -*- coding: utf-8 -*-
# JESSE RUBIN - project Euler
from math import sqrt
from operator import truediv, methodcaller
from lib.maths import gcd, Vuple
from sys import version_info

if version_info.major > 2:  # py2/3 range/xrange
    xrange = range


def pytriple_gen(max_c, primatives_only=True):
    """
    primative pythagorean triples generator

    thanks to 3Blue1Brown
    special thanks to 3Blue1Brown's video on pythagorean triples
    https://www.youtube.com/watch?v=QJYmyhnaaek&t=300s

    :param max_c:
    :return:
    """
    for real_pts in xrange(2, int(sqrt(max_c)) + 1, 1):
        for imag_pts in xrange(real_pts % 2 + 1, real_pts, 2):
            comp = complex(real_pts, imag_pts)
            sqrd = comp * comp
            real = int(sqrd.real)
            imag = int(sqrd.imag)
            if abs(real - imag) % 2 == 1 and gcd(imag, real) == 1:
                sea = int((comp * comp.conjugate()).real)
                if sea > max_c:
                    break
                else:
                    yield (imag, real, sea) if real > imag else (real, imag, sea)


# def triangle_area(v1, v2):
#     return abs(cproduct(v1, v2)) / 2


class Trigon(object):

    def __init__(self, pt1, pt2, pt3):
        # if len(pts) == 3:
        #     self.pt1 = Vuple(pts[0])
        #     self.pt2 = Vuple(pts[1])
        #     self.pt3 = Vuple(pts[2])
        # elif len(pts) == 1:
        #     a, b, c = pts[0]
        #     self.pt1 = Vuple(a)
        #     self.pt2 = Vuple(b)
        #     self.pt3 = Vuple(c)
        self.pt1 = Vuple(pt1)
        self.pt2 = Vuple(pt2)
        self.pt3 = Vuple(pt3)

    @classmethod
    def from_points(cls, pts):
        if len(pts) == 3:
            return Trigon(*pts)
        if len(pts) == 6:
            it = iter(pts)
            return Trigon(*zip(it, it))

    def __str__(self):
        return "pt1~{}; pt2~{}; pt3~{}".format(self.pt1, self.pt2, self.pt3)

    def __contains__(self, point):
        if type(point) is not Vuple:
            point = Vuple(point)
        return self.area() == sum(map(methodcaller('area'),
                                      self.inner_triangles(point)))

    def inner_triangles(self, point):
        t1 = Trigon(point, self.pt2, self.pt3)
        t2 = Trigon(self.pt1, point, self.pt3)
        t3 = Trigon(self.pt1, self.pt2, point)
        return t1, t2, t3

    def points_set(self):
        return {self.pt1, self.pt2, self.pt3}

    def __eq__(self, other):
        """Tests equality by testing if sets of points are equal

        :param other:
        :return:
        """
        return self.points_set() == other.points_set()

    def points(self):
        return self.pt1, self.pt2, self.pt3

    def contains_origin(self):
        return (0, 0) in self

    def area(self):
        return abs(truediv(Vuple.cross(self.pt1 - self.pt2,
                                       self.pt3 - self.pt2), 2))

    @staticmethod
    def area_from_points(pt1, pt2, pt3):
        return abs(truediv(Vuple.cross(pt1 - pt2, pt3 - pt2), 2))


print(Trigon((1, 2), (1, 3), (0, 0)))
print(Trigon.from_points([(1, 2), (1, 3), (0, 0)]))
print(Trigon.from_points([1, 2, 1, 3, 0, 0]))