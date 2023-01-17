from sympy import diff, symbols
from typing import List


class Point_2d:
    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y

    def __eq__(self, other):
        return (self.coordinate_x == other.coordinate_x and
                self.coordinate_y == other.coordinate_y)

    def __str__(self):
        return f'X:{self.coordinate_x}, Y:{self.coordinate_y}'

    def __repr__(self):
        return f'X:{self.coordinate_x}, Y:{self.coordinate_y}'


class Curve:
    '''Curve meta class'''
    t = symbols('t')

    def points(self, t_value: float) -> List[Point_2d]:
        points = [Point_2d(t_value, x.subs(self.t, t_value)) for x in self.c]
        return points

    def derivatives(self, t_value: float) -> List[float]:
        solutions = [x.subs(self.t, t_value) for x in self.diff_c]
        return solutions


class Line(Curve):
    '''Line class'''
    def __init__(self, origin_point: float, direction: float) -> None:
        self.origin_point = origin_point
        self.direction = direction
        self.c = [self.origin_point + self.direction * self.t]
        self.diff_c = [diff(x, self.t) for x in self.c]

    def __str__(self):
        return f'Line C(t) = {self.c[0]}'


class Ellipse(Curve):
    '''Ellipse class'''
    def __init__(self, radius_x: float, radius_y: float) -> None:
        if (radius_x <= 0 or radius_y <= 0):
            raise ValueError('radius should be positive')
        self.radius_x = radius_x
        self.radius_y = radius_y
        c_mod = self.radius_y / self.radius_x * (self.radius_x ** 2 -
                                                 self.t ** 2)**0.5
        self.c = [c_mod, -c_mod]
        self.diff_c = [diff(x, self.t) for x in self.c]

    def points(self, t_value: float) -> List[float]:
        if (self.radius_x ** 2 - t_value ** 2) < 0:
            return []
        if (self.radius_x == t_value):
            return super().points(t_value)[0:1]
        return super().points(t_value)

    def derivatives(self, t_value: float) -> List[float]:
        if (self.radius_x ** 2 - t_value ** 2) <= 0:
            return []
        return super().derivatives(t_value)

    def __str__(self):
        return f'Ellipse Rx = {self.radius_x}, Ry = {self.radius_y}'
