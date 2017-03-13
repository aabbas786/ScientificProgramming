from gjtools import *
from fractions import Fraction

m = [[Fraction(1, 1), Fraction(2, 1), Fraction(3, 1), Fraction(0, 1)],
     [Fraction(3, 1), Fraction(4, 1), Fraction(7, 1), Fraction(2, 1)],
     [Fraction(6, 1), Fraction(5, 1), Fraction(9, 1), Fraction(11, 1)]]

#m = [[3, 3, 8, 1], [3, -1, 3, 3], [5 ,7 ,-1 ,16]]

print_matrix(m)

reduced_row_echelon(m)
print_matrix(m)
exit()

# Set first value in row 1 to 1
mul_row(m, Fraction(1, m[0][0]), 1)
print_matrix(m)

# multiply row 1 by the first element of row 2 and add it to row 2
add_row(m, -m[1][0], 1, 2)
print_matrix(m)


add_row(m, -m[2][0], 1, 3)
print_matrix(m)


mul_row(m, Fraction(1, m[1][1]), 2)
print_matrix(m)


add_row(m, -m[2][1], 2, 3)
print_matrix(m)

mul_row(m, Fraction(1, m[2][2]), 3)
print_matrix(m)

add_row(m, -m[1][2], 3, 2)
print_matrix(m)

add_row(m, -m[0][2], 3, 1)
print_matrix(m)

add_row(m, -m[0][1], 2, 1)
print_matrix(m)
