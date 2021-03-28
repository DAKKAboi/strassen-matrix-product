from SubMatrixOperations import *
from matrixOperations import *
from strass import *
from RandomSquareMatrix import *

#matrixA = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0],[0, 0, 0, 1]]
#matrixB = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0],[0, 0, 0, 1]]

#matrixA = [[1, 0], [0, 1]]
#matrixB = [[2, 3], [5, 7]]

matrixA = randMatrix(64, 100)
matrixB = randMatrix(64, 100)

print(matrixA)

print(strassenMethod(matrixA, matrixB))




