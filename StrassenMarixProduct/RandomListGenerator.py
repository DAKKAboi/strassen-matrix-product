def listGen(listLen, min, max):
    import random
    randList = [0]*listLen
    i = 0
    while i<= (listLen-1):
        randList[i] = random.randint(min,max)
        i=i+1
    return(randList)
