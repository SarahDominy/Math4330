def matrixvector(matrixa,vectorx):
    """
    Multiplies a matrix by a vector.
    
    Args:
        A matrix representing a list of vectors and a vector representing a list of numbers.
    Returns:
        A matrix where all of the vectors have been multiplied by the vector input.
    """
    result = [0] * len(matrixa[0])
    for i in range (len(vectorx)):
        result = vectoradd(result,scalarvectormult(vectorx[i],matrixa[i]))
    return result
