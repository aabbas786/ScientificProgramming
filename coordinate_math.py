import math

def cartesian_to_polar(p):
    """
    convert a point provided as an ordered 2-tuple representing the cartesian
    coordinates to the same point in polar coordinates.

      >>> cartesian_to_polar((3, 4))
      (5.0, 0.9272952180016122)
      >>> cartesian_to_polar((5, 12))
      (13.0, 1.176005207095135)
    """
    x, y = p 
    r = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    theta = math.atan(y / x)
    return r, theta

def polar_to_cartesian(p):
    """
    >>> coord = polar_to_cartesian((3, math.pi))
    >>> round(coord[0])
    -3
    >>> round(coord[1])
    0
    >>> coord = polar_to_cartesian((2, math.pi/ 2))
    >>> round(coord[0])
    0
    >>> round(coord[1])
    2
    """
    r = p[0]
    theta = p[1]
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return x, y

if __name__ == '__main__':
    import doctest
    doctest.testmod()


def str2point(point_str):
    x, y = point_str.split(', ')
    return (int(x), int(y))


def convert_cartesian_point(fname, line_num):
    io = open(fname, "r")
    point_str = io.readlines()[line_num - 1][:-1]
    points = point_str.split('), ')
    points = [point[1:] for point in points]
    points[-1] = points[-1][:-1]
    points = [str2point(point) for point in points]
    return points

print(convert_cartesian_point('cartesian_points.dat', 1))
