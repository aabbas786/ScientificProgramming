def add_point(matrix, point, value=1):
    """
      >>> sparse = {}
      >>> add_point(sparse, (172, 358), 2)
      >>> (172, 358) in sparse
      True
      >>> sparse[(172, 358)]
      2
      >>> add_point(sparse, (200, 100))
      >>> sparse[(200, 100)]
      1
      >>> add_point(sparse, (172, 358), 10)
      >>> sparse[(172, 358)]
      12
      >>> sparser = {}
      >>> add_point(sparser, (1000000, 5000000))
      >>> sparser[(1000000, 5000000)]
      1
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod()
