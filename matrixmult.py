def vectorAddition(vectora,vectorb):
    """
    This algorithm calculates the sum of two vectors.
    Args:
        Two vectors, each representing a list of numbers
    Returns:
        A vector that is the sum of both vectors.
    """
    if len(vectora) > len(vectorb):
        resultant = vectora
        for i in range (0,len(vectorb)):
            resultant[i] = resultant[i] + vectorb[i]
    else:
        resultant = vectorb
        for i in range (0,len(vectora)):
            resultant[i] = resultant[i] + vectora[i]
    return resultant      

def scalarvectormult(vectora,scalarb):
    """
    This algorithm multiplies a vector by a scalar value
    
    Args:
        A vector representing a list of numbers and one scalar number.
    Returns:
        A vector where each of the values has been multiplied by the scalar.
    """
    result = [0] * len(vectora)
    for i in range (len(vectora)):
        result[i] = vectora[i] * scalarb
    return result


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
        result = vectorAddition(result,scalarvectormult(matrixa[i],vectorx[i]))
    return result



def matrixmult(matrixa,matrixb):
    """
    Multiplies a matrix by a matrix

    Args:
          Two matrices representing two lists of vectors.
    Returns:
          A matrix that is the product of multiplying matrixa and matrixb
    """
    if len(matrixa) == len(matrixb[0]):
        result = [[0] * len(matrixa)]*len(matrixb[0])
        for i in range(len(matrixa)):
            result[i] = matrixvector(matrixb,matrixa[i])
    print (result)




X = [[1,2,1],[1,3,1],[1,4,1]]
Y = [[7,8,9],[9,10,11],[11,12,13]]
matrixmult(X,Y)
