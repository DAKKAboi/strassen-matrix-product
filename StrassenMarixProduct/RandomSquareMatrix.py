from RandomListGenerator import *

def randMatrix(width, range):
    i = 0
    A = [0]*width

    while i < width:
        A[i] = listGen(width, -range, range)
        i = i + 1

    return A
