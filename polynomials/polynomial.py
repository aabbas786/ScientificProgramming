def print_poly(p):
    """
      >>> print_poly([4, 3, 2])
      '4x^2 + 3x + 2'
      >>> print_poly([2, 8, 3])
      '2x^2 + 8x + 3'
      >>> print_poly([8, 6, 7, 9])
      '8x^3 + 6x^2 + 7x + 9'
    """
    polystr = ''    
    expon = len(p) - 1 
    
    for i in range(len(p)):
        if expon == 0:
            polystr += str(p[-1])
        elif expon == 1:
            polystr += str(p[-2]) + 'x + '
        else:
            polystr += '{0}x^{1} + '.format(p[i], expon)
        expon -= 1
    
    return polystr


if __name__ == '__main__':
    import doctest
    doctest.testmod()
