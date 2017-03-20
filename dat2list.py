def bella(filename):
    """
    So, basically all this function does is, it gets a filename of a file that exists in the working parent directory. and it returns a list of matrices (list of lists). Matrices are separated a by '##' and each row is separated by a new line. The numbers, MARCO, are separated by semi-colons(;).
    """
    filecontents = open(filename, "r").read()
    adell = filecontents.split("##")
    for i in range(len(adell)):
        adell[i] = adell[i].strip().split("\n")
        for j in range(len(adell[i])):
            adell[i][j] =  adell[i][j].split(";")
            for k in range(len(adell[i][j])):
                adell[i][j][k] = int(adell[i][j][k])
    print(adell)


bella("matrices.dat")

marco = [[[3, -2, 5, 31], [1, 3, -3, -12], [-2, -5, 3, 11]], 
        [[2, 1, 3, 3], [3, -5, -1, 4], [1, -2, -3, -6]],
        [[3, -1, -4, 3], [2, -1, 2, -8], [1, 2, -3, 9]]]

print(marco)

