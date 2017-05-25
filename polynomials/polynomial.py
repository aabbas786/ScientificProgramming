def get_opp(p, i):
    """
    """
    """
      >>> get_opp([7, -3, 5, -6], 0)
      ''
      >>> get_opp([7, -3, 5, -6], 1)
      ' - '
      >>> get_opp([7, -3, 5, -6], 2)
      ' + '
      >>> get_opp([7, -3, 5, -6], 3)
      ' - '
    """


def get_xterm(p, i):
    """
      >>> get_xterm([8, 6, 7, 9], 0)
      'x^3'
      >>> get_xterm([1, 8, 6, 7, 9], 2)
      'x^2'
      >>> get_xterm([1, 8, 6, 7, 9], 0)
      'x^4'
    """
    """
      >>> get_xterm([8, 6, 7, 9], 2)
      'x'
      >>> get_xterm([8, 6, 7, 9], 3)
      ''
    """


def poly_to_str(p):
    """
    """
    """
      >>> poly_to_str([4, 3, 2])
      '4x^2 + 3x + 2'
      >>> poly_to_str([2, 8, 3])
      '2x^2 + 8x + 3'
      >>> poly_to_str([8, 6, 7, 9])
      '8x^3 + 6x^2 + 7x + 9'
      >>> poly_to_str([7, -3, 5, -6])
      '7x^3 - 3x^2 + 5x - 6'
    """
    polystr = ''

    for i in range(len(p)):
        coeff = str(abs(p[i]))
        xterm = get_xterm(p, i)
        opp = get_opp(p, i)
        polystr += '{0}{1}{2}'.format(coeff, xterm, opp)

    return polystr


if __name__ == '__main__':
    import doctest
    doctest.testmod()
