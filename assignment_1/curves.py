from models import Ellipse, Line

from math import pi


if __name__ == '__main__':
    t = pi / 4
    container = [
        Line(0, 0),
        Line(3, 5),
        Line(-3, 5),
        Line(3, -5),
        Line(-3, -5),
        Line(15.3, 7.6),
        Line(-15.3, 7.6),
        Line(15.3, -7.6),
        Line(-15.3, -7.6),
        Ellipse(1, 1),
        Ellipse(12, 12),
        Ellipse(12.1, 3),
        Ellipse(3, 12.5),
        Ellipse(105.8, 7.4),
    ]
    for curve in container:
        print(curve)
        print('  Points at t=PI/4:')
        for point in curve.points(t):
            print('   ', point)
        print('  Derivates at t=PI/4:')
        for derivative in curve.derivatives(t):
            print('   ', derivative)
        print('\n')
