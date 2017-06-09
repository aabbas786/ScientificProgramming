def get_opp(p, i):
    """
      >>> get_opp((7, -3, 5, -6), 1)
      ' - '
      >>> get_opp((7, -3, 5, -6), 2)
      ' + '
      >>> get_opp((7, -3, 5, -6), 3)
      ' - '
      >>> get_opp((7, -3, 5, -6), 0)
      ''
      >>> get_opp((-3, 5, -6), 0)
      '-'
    """
    if i == 0:
        if p[0] > 0:
            return ''
        else:
            return '-'
    if p[i] > 0:
        return ' + '
    else:
        return ' - '


def get_xterm(p, i):
    """
      >>> get_xterm((8, 6, 7, 9), 0)
      'x^3'
      >>> get_xterm((1, 8, 6, 7, 9), 2)
      'x^2'
      >>> get_xterm((1, 8, 6, 7, 9), 0)
      'x^4'
      >>> get_xterm((8, 6, 7, 9), 2)
      'x'
      >>> get_xterm((8, 6, 7, 9), 3)
      ''
    """
    exp = len(p) - (i + 1)
    if exp == 1:
        return 'x'
    if exp == 0:
        return ''
    return 'x^{0}'.format(exp)
    

def poly_to_str(p):
    """
      >>> poly_to_str((4, 3, 2))
      '4x^2 + 3x + 2'
      >>> poly_to_str((2, 8, 3))
      '2x^2 + 8x + 3'
      >>> poly_to_str((8, 6, 7, 9))
      '8x^3 + 6x^2 + 7x + 9'
      >>> poly_to_str((7, -3, 5, -6))
      '7x^3 - 3x^2 + 5x - 6'
      >>> poly_to_str((5, 0, 2))
      '5x^2 + 2'
      >>> poly_to_str((-7, 0, 3, 5, 0, -2))
      '-7x^5 + 3x^3 + 5x^2 - 2'
      >>> poly_to_str((-7, 0, 0, 5, 0, 0))
      '-7x^5 + 5x^2'
    """
    polystr = ''

    for i in range(len(p)):
        coeff = abs(p[i])
        if coeff == 0:
            continue
        xterm = get_xterm(p, i)
        opp = get_opp(p, i)
        polystr += '{0}{1}{2}'.format(opp, coeff, xterm)

    return polystr


def add_polys(p1, p2):
    """
      >>> add_polys((3, 1, 2), (1, 2, 3))
      (4, 3, 5)
      >>> poly_to_str(add_polys((4, 3, 5, 9), (2, -3, 2, -9)))
      '6x^3 + 7x'
      >>> add_polys((5, 3, 1, 2), (1, 2, 3))
      (5, 4, 3, 5)
      >>> add_polys((5, 3), (1, 2, 3, 4))
      (1, 2, 8, 7)
    """
    if len(p1) < len(p2):
        p1 = ((0, ) * (len(p2) - len(p1))) + p1
    elif len(p2) < len(p1):
        p2 = ((0, ) * (len(p1) - len(p2))) + p2
    p3 = []
    for i in range(len(p1)):
        p3.append(p1[i] + p2[i])
    
    return tuple(p3)


def term_x_poly(coeff, exp, p):
    """
      >>> term_x_poly(4, 2, (3, 0, 2, 0, 0, 0))
      (12, 0, 8, 0, 0, 0, 0, 0)
    """
    prod = []

    for c in p:
        prod.append(coeff * c)

    return tuple(prod) + (0, ) * exp


def mul_polys(p1, p2):
    """
      >>> mul_polys((4, -5), (2, 3, -6))
      (8, 2, -39, 30)
      >>> mul_polys((3, 2), (5, 6))
      (15, 28, 12)
      >>> mul_polys((4, 0, 5, 3), (7, 4, 0, 5))
      (28, 16, 35, 61, 12, 25, 15)
      >>> mul_polys((0, 4), (4, 0))
      (16, 0)
      >>> mul_polys((0, 0, 0, 0, 0, 4), (4, 0, 0, 0, 0, 0))
      (16, 0, 0, 0, 0, 0)
      >>> mul_polys((-4, 3), (7, 5))
      (-28, 1, 15)
    """
    p3 = ()
    not0i = 0
    for i in range(len(p1)):
        bigpoly = term_x_poly(p1[i], len(p1) - 1 - i, p2)
        p3 = add_polys(bigpoly, p3)

    while p3[not0i] == 0:
        not0i += 1

    return p3[not0i:]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
