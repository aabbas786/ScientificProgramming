def print_poly(p):
    """
      >>> print_poly([4, 3, 2])
      '4x^2 + 3x + 2'
      >>> print_poly([2, 8, 3])
      '2x^2 + 8x + 3'
      >>> print_poly([8, 6, 7, 9])
      '8x^3 + 6x^2 + 7x + 9'
      >>> print_poly([7, -3, 5, -6])
      '7x^3 - 3x^2 + 5x - 6'
    """
    polystr = ''    
    expon = len(p) - 1 
    
    for i in range(len(p)):
        coeff = str(p[i])
        if i == len(p) - 1:
            polystr += coeff
            break

        expon -= 1
    
        polystr += '{0}{1}{2}'.format(coeff, expon, opp)

    return polystr


if __name__ == '__main__':
    import doctest
    doctest.testmod()
