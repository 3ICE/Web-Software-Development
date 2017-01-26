from math import pi, sqrt

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def distance_from(self, o):
        return sqrt((self._x - o._x)**2 + (self._y - o._y)**2)

class Circle:
    def __init__(self, p, r):
        self._p = p
        self._r = r

    @property
    def radius(self):
        return self._r

    @property
    def center (self):
        return self._p

    def is_inside(self, o):
        return _p.distance_from(o) < self._r
