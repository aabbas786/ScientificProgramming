import math

def cartesian_to_polar(x, y):
    r = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    theta = math.atan(y / x)
    return r, theta

print(cartesian_to_polar(2, 2))

def str2point(point_str):
    x, y = point_str.split(', ')
    return (int(x), int(y))
def read_point_set_from_file(fname, line_num):
    io = open(fname, "r")
    point_str =  io.readlines()[line_num - 1][:-1]
    points = point_str.split('), ')
    points = [point[1:] for point in points]
    points[-1] = points[-1][:-1]
    points = [str2point(point) for point in points]
    return points
read_point_set_from_file("cartesian_points.dat", 1)
