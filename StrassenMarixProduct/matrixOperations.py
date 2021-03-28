def addMatrices(A, B):
    #the matrices both have to be square and have the same dimensions

    width = int(len(A))
    C = zeroes(width)

    j = 0
    while j <= (width - 1):
        i = 0
        while i <= (width - 1):
            C[i][j] = A[i][j] + B[i][j]
            i = i + 1
        j = j + 1

    return C

def subtractMatrices(A, B):
    #the matrices both have to be square and have the same dimensions
    #returns C = A - B

    width = len(A)
    C = zeroes(width)

    j = 0
    while j <= width - 1:
        i = 0
        while i <= width - 1:
            C[i][j] = A[i][j] - B[i][j]
            i = i + 1
        j = j + 1

    return C

def zeroes(width):
    A = []
    i = 0
    while i <= width - 1:
        A.append([0]*width)
        i = i + 1
    return A
