def str2point(point_str):
    """
    Convert a string with two comma seperated numbers into a tuple of
    two numbers.

      >>> type(str2point('1, 2'))
      <class 'tuple'>
      >>> str2point('1, 2')
      (1, 2)
    """
    x, y = point_str.split(', ')
    return (int(x), int(y))


def read_point_set_from_file(fname, line_num):
    """
    Read in a set of 3 points at line_num from the fname file and convert
    them to a list of 2-tuples.

      >>> read_point_set_from_file('test_point_sets.dat', 1)
      [(-3, -65), (4, -16), (-10, -408)]
      >>> read_point_set_from_file('test_point_sets.dat', 2)
      [(-2, -40), (3, -5), (5, -33)]
    """
    f = open(fname, 'r')
    # read in a line containing three points, stripping off the \n
    # Example: '(-3, -65), (4, -16), (-10, -408)'
    point_str =  f.readlines()[line_num - 1][:-1]
    # create a list of the three point strings by splitting on '), '
    # Example: ['(-3, -65', '(4, -16', '(-10, -408)']
    points = point_str.split('), ')
    # Remove the '(' at the beginning of each point
    # Example: ['-3, -65', '4, -16', '-10, -408)']
    points = [point[1:] for point in points]
    # Remove the ')' at the beginning of the last point
    # Example: ['-3, -65', '4, -16', '-10, -408']
    points[-1] = points[-1][:-1]
    # call str2point to turn the strings into 2-tuples with numbers
    points = [str2point(point) for point in points]

    return points



if __name__ == '__main__':
    import doctest
    doctest.testmod()
