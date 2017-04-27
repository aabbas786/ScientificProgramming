from gjtools import print_matrix, mul_row, add_row
from fractions import Fraction

#messed up this matrix it wasnt this one m = [[9, -3, 1, -65], [16, 4, 1, -16], [100, -10, 1, -408]]
print_matrix(m)
mul_row(m, Fraction(1, 2), 3)
print_matrix(m)
add_row(m, 1, 1, 2)
add_row(m, -1, 1, 3)
print_matrix(m)
add_row(m, Fraction(1, 2), 2, 3)
print_matrix(m)
add_row(m, -3, 3, 2)
add_row(m, -3, 3, 1)
print_matrix(m)
add_row(m, 2, 2, 1)
print_matrix(m)
