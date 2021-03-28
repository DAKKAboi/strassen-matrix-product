from matrixOperations import *

def matrixSplit(bigMatrix):
    #this  function splits a 2^n*2^n into four smaller square matrices, one for each corner
    #the matrix is represented by an n long array filled with n long arrays

    n = len(bigMatrix)

    splitPoint = int(n/2 -1)

    def looper(bigMatrix, xStart, xStop, yStart, yStop):

        smallMatrixN = int(len(bigMatrix)/2)

        smallMatrix = zeroes(smallMatrixN)

        i = yStart
        while i <= yStop:
            j = xStart
            while j <= xStop:
                smallMatrix[j - xStart][i - yStart] = bigMatrix[j][i]
                j = j + 1
            i = i + 1

        return smallMatrix
    
    topLeft = looper(bigMatrix, 0, splitPoint, 0, splitPoint)
    topRight = looper(bigMatrix, splitPoint + 1, n - 1, 0, splitPoint)
    bottomLeft = looper(bigMatrix, 0, splitPoint, splitPoint + 1, n - 1)
    bottomRight = looper(bigMatrix, splitPoint + 1, n - 1, splitPoint + 1, n - 1)

    return [topLeft, bottomLeft, topRight, bottomRight]

def findSMatrices(a11, a12, a21, a22, b11, b12, b21, b22):
    s1 = subtractMatrices(b12, b22) 
    s2 = addMatrices(a11, a12)
    s3 = addMatrices(a21, a22)
    s4 = subtractMatrices(b21, b11 )
    s5 = addMatrices(a11, a22 )
    s6 = addMatrices(b11, b22 )
    s7 = subtractMatrices(a12, a22 )
    s8 = addMatrices(b21, b22)
    s9 = subtractMatrices(a11, a21) 
    s10 = addMatrices(b11, b12) 

    return s1, s2, s3, s4, s5, s6, s7, s8, s9, s10

def combineMatrices(a11, a12, a21, a22):
    widthBig = 2*len(a11)
    widthSmall = len(a11)

    def looper(bigMatrix, smallMatrix, xStart, yStart):

        smallWidth = len(smallMatrix)

        i = yStart
        while i <= (yStart + smallWidth - 1):
            j = xStart
            while j <= (xStart + smallWidth - 1):
                bigMatrix[j][i] = smallMatrix[j - xStart][i - yStart]
                j = j + 1
            i = i + 1
        return bigMatrix
    
    A = zeroes(widthBig)


    A = looper(A, a11, 0, 0)
    A = looper(A, a21, widthSmall, 0)
    A = looper(A, a12, 0, widthSmall)
    A = looper(A, a22, widthSmall, widthSmall)

    return A

