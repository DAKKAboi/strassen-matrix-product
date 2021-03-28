from matrixOperations import *
from SubMatrixOperations import *

def strassenMethod(A, B):
    print('strass')
    print('A = ' + str(A))
    print('B = ' + str(B))

    if len(A) == 1:
        a = A[0][0]
        b = B[0][0]
        return [[a*b]]

    else:
        a11, a12, a21, a22 = matrixSplit(A)
        b11, b12, b21, b22 = matrixSplit(B)
        s1, s2, s3, s4, s5, s6, s7, s8, s9, s10 = findSMatrices(a11, a12, a21, a22, b11, b12, b21, b22)        

        p1 = strassenMethod(a11, s1)
        p2 = strassenMethod(s2, b22)
        p3 = strassenMethod(s3, b11)
        p4 = strassenMethod(a22, s4)
        p5 = strassenMethod(s5, s6)
        p6 = strassenMethod(s7, s8)
        p7 = strassenMethod(s9, s10)

        c11 = subtractMatrices(addMatrices(p5, p4), subtractMatrices(p2, p6))
        c12 = addMatrices(p1, p2)
        c21 = addMatrices(p3, p4)
        c22 = subtractMatrices(addMatrices(p5, p1), addMatrices(p3, p7))

        C = combineMatrices(c11, c12, c21, c22)

        print('C = ' + str(C))
        return C
