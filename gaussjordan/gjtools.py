from fractions import Fraction

def print_matrix(m):
    for row in m:
        print('|{0:6s}{1:6s}{2:6s}|{3:6s}|'.format(*[str(val) for val in row]))
    print()


def mul_row(m, k, ri):
    for i in range(len(m[ri])):
        m[ri][i] *= k


def add_row(m, k, ri, rj):
    for i in range(len(m[ri])):
        m[rj][i] += k * m[ri][i]

def lead_coeff_to_one(m, row_coeff):
    row_num = len(m)
    # Multiply the row <row> by the multiplicative inverse
    # of the <row>th element
    mul_row(m, Fraction(1, m[row_coeff][row_coeff]), row_coeff)
    #Zero the other <row_num> rows on column <row>
    for i in range(1, row_num):
        row = (row_coeff + i) % row_num
        add_row(m, -m[row][row_coeff], row_coeff, row)

def reduced_row_echelon(m):
    """
    Transform augmented matrix m to reduced row echelon form.
      >>> matrix = reduced_row_echelon([
      ...         [1, -2, 3, 9],
      ...         [-1, 3, 0, -4],
      ...         [2, -5, 5, 17]
      ...         ])

      >>> print_matrix(matrix)
      |1     0     0     |1     |
      |0     1     0     |-1    |
      |0     0     1     |2     |
      <BLANKLINE>
    """

    for index in range(len(m)):
        lead_coeff_to_one(m, index)

    return m

if __name__ == '__main__':
    import doctest
    #doctest.testfile("gjtest")
    doctest.testmod()
