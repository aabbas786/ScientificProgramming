import math


def cartesian_to_polar(p):
    """
    Convert a point provided as an ordered 2-tuple representing the cartesian
    coordinates to the same point in polar coordinates.

      >>> cartesian_to_polar((3, 4))
      (5.0, 0.9272952180016122)
      >>> cartesian_to_polar((5, 12))
      (13.0, 1.176005207095135)
    """
    r = (p[0] ** 2 + p[1] ** 2) ** 0.5
    theta = math.atan2(p[1], p[0])

    return (r, theta)


def polar_to_cartesian(p):
    """
    Convert a point provided as an ordered 2-tuple representing the polar
    coordinates to the same point in cartesian coordinates.

      >>> p = polar_to_cartesian((5, 0.9272952180016122))
      >>> int(round(p[0]))
      3
      >>> int(round(p[1]))
      4
      >>> p2 = polar_to_cartesian((13, 1.17605207095135))
      >>> int(round(p2[0]))
      5
      >>> int(round(p2[1]))
      12
    """
    r, theta = p[0], p[1]

    return r * math.cos(theta), r * math.sin(theta)


def parse_points(fp):
    """
    Read in points represented as text and convert them to numeric tuples

      >>> import io
      >>> fp = io.StringIO("(3, 4)\\n(5, 12)\\n(15, 8)\\n(28, 45)\\n")
      >>> points = parse_points(fp)
      >>> type(points)
      <class 'list'>
      >>> len(points)
      4
      >>> p1 = points[0]
      >>> p1
      (3, 4)
      >>> points[-1][-1]
      45
    """
    points = fp.readlines()
    for i in range(len(points)):
        points[i] = points[i].strip("( \n)")
        points[i] = points[i].split(', ')
        points[i] = int(points[i][0]), int(points[i][1])
    return points


if __name__ == '__main__':
    import doctest
    doctest.testmod()
