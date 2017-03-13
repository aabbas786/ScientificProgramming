from fractions import Fraction

def print_matrix(m):
    for row in m:
        print('|{0:6s}{1:6s}{2:6s}|{3:6s}|'.format(*[str(val) for val in row]))
    print()


def mul_row(m, k, ri):
    for i in range(len(m[ri-1])):
        m[ri-1][i] *= k


def add_row(m, k, ri, rj):
    for i in range(len(m[ri-1])):
        m[rj-1][i] += k * m[ri-1][i]


def reduced_row_echelon(m):
    """Transform augmented matrix m to reduced row echelon form."""

    # Set first value in row 1 to 1
    mul_row(m, Fraction(1, m[0][0]), 1)

    # multiply row 1 by the first element of row 2 and add it to row 2
    add_row(m, -m[1][0], 1, 2)

    add_row(m, -m[2][0], 1, 3)

    mul_row(m, Fraction(1, m[1][1]), 2)

    add_row(m, -m[2][1], 2, 3)

    mul_row(m, Fraction(1, m[2][2]), 3)

    add_row(m, -m[1][2], 3, 2)

    add_row(m, -m[0][2], 3, 1)

    add_row(m, -m[0][1], 2, 1)
    print_matrix(m)

if __name__ == '__main__':
    import doctest
    doctest.testfile("gjtest")
