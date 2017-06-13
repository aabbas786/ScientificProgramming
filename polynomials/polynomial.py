class Polynomial:
    """
      >>> p = Polynomial()
      >>> type(p)
      <class '...Polynomial'>
      >>> p = Polynomial((3, 4, 1))
      >>> p.coeffs
      (3, 4, 1)
    """
    """
      >>> p.poly_to_str()
      '3x^2 + 4x + 1'
    """
    def __init__(self, coeffs=(0,)):
        self.coeffs = coeffs


    def get_opp(self, i):
        """
          >>> p = Polynomial((7, -3, 5, -6))
          >>> p.get_opp(1)
          ' - '
          >>> p.get_opp(2)
          ' + '
          >>> p.get_opp(3)
          ' - '
          >>> p.get_opp(0)
          ''
          >>> p2 = Polynomial((-3, 5, -6))
          >>> p2.get_opp(0)
          '-'
        """
        if i == 0:
            if self.coeffs[0] > 0:
                return ''
            else:
                return '-'
        if self.coeffs[i] > 0:
            return ' + '
        else:
            return ' - '


    def get_xterm(self, i):
        """

          >>> p = Polynomial((8, 6, 7, 9))
          >>> p.get_xterm(0)
          'x^3'
          >>> p.get_xterm(2)
          'x'
          >>> p.get_xterm(3)
          ''
          >>> p2 = Polynomial((1, 8, 6, 7, 9))
          >>> p2.get_xterm(2)
          'x^2'
          >>> p2.get_xterm(0)
          'x^4'
        """
        exp = len(self.coeffs) - (i + 1)
        if exp == 1:
            return 'x'
        if exp == 0:
            return ''
        return 'x^{0}'.format(exp)


    def __repr__(self):
        """
          >>> p = Polynomial((4, 3, 2))
          >>> p
          4x^2 + 3x + 2
          >>> p2 = Polynomial((2, 8, 3))
          >>> print(p2)
          2x^2 + 8x + 3
          >>> p3 = Polynomial((8, 6, 7, 9))
          >>> p3
          8x^3 + 6x^2 + 7x + 9
          >>> p4 = Polynomial((7, -3, 5, -6))
          >>> p4
          7x^3 - 3x^2 + 5x - 6
          >>> p5 = Polynomial((5, 0, 2))
          >>> print(p5)
          5x^2 + 2
          >>> p6 = Polynomial((-7, 0, 3, 5, 0, -2))
          >>> p6
          -7x^5 + 3x^3 + 5x^2 - 2
          >>> p7 = Polynomial((-7, 0, 0, 5, 0, 0))
          >>> p7
          -7x^5 + 5x^2
        """
        polystr = ''

        for i in range(len(self.coeffs)):
            coeff = abs(self.coeffs[i])
            if coeff == 0:
                continue
            xterm = self.get_xterm(i)
            opp = self.get_opp(i)
            polystr += '{0}{1}{2}'.format(opp, coeff, xterm)

        return polystr


    def __add__(self, other):
        """
          >>> p1 = Polynomial((3, 1, 2))
          >>> p2 = Polynomial((1, 2, 3))
          >>> p1 + p2
          4x^2 + 3x + 5
          >>> p3 = Polynomial((4, 3, 5, 9))
          >>> p4 = Polynomial((2, -3, 2, -9))
          >>> (p3 + p4).coeffs
          (6, 0, 7, 0)
          >>> p5 = Polynomial((5, 3, 1, 2))
          >>> p6 = Polynomial((1, 2, 3))
          >>> (p5 + p6).coeffs
          (5, 4, 3, 5)
        """
        if len(self.coeffs) < len(other.coeffs):
            coeffs1 = ((0, ) * (len(other.coeffs) - len(self.coeffs))) + \
                    self.coeffs
            coeffs2 = other.coeffs
        elif len(other.coeffs) < len(self.coeffs):
            coeffs2 = ((0, ) * (len(self.coeffs) - len(other.coeffs))) + \
                    other.coeffs
            coeffs1 = self.coeffs
        else:
            coeffs1 = self.coeffs
            coeffs2 = other.coeffs
        sumcoeffs = []
        for i in range(len(coeffs1)):
            sumcoeffs.append(coeffs1[i] + coeffs2[i])
        
        return Polynomial(tuple(sumcoeffs))


    def mult_by_term(self, coeff, exp):
        """
          >>> p = Polynomial((1, 2, 3))
          >>> p.mult_by_term(4, 2).coeffs
          (4, 8, 12, 0, 0)
        """
        prod = []

        for c in self.coeffs:
            prod.append(coeff * c)

        prod += [0] * exp

        return Polynomial(tuple(prod))

    def mul_polys(self, other):
        """
          >>> p1 = Polynomial((4, -5))
          >>> p2 = Polynomial((2, 3, -6))
          >>> mul_polys(p1, p2)
          (8, 2, -39, 30)
        """
        """
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
    doctest.testmod(optionflags=doctest.ELLIPSIS)
