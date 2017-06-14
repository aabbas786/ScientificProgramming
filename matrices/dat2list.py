def from_memory(filename):
    filepointer = open(filename, 'r')
    filecontent = filepointer.read()
    filepointer.close()
    raw_matrices = filecontent.split("##")
    raw_matrices = [item.strip() for item in raw_matrices] 
    raw_matrices = [item.split("\n") for item in raw_matrices]
    m = []
    for matrix in raw_matrices:
        m.append([row.split(";") for row in matrix])
    for matrix in m:
        for i, row in enumerate(matrix):
            matrix[i] = [int(elem) for elem in row]

    return m
