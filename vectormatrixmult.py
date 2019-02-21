def matrixvector(matrixa,vectorx):
    result = [0] * len(matrixa[0])
    for i in range (len(vectorx)):
        result = vectoradd(result,scalarvectormult(vectorx[i],matrixa[i]))
    return result
