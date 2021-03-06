a = [1, 2, 3]
def twonorm(vectora):
    """This function calculates the two norm of a vector
        it does so by squaring all the values in the vector 
        and adding them together and then taking the square root
        of the sum.
        args:
        a vector representing a list of numbers
        returns:
        a scalar that is the two norm of the vector
    """
    result = 0
    for i in range (0,len(vectora)):
            result = result + vectora[i] ** 2
    result = result ** (0.5)
    return result
def scalarvectormult(vectora,scalarb):
    """
    This algorithm multiplies a vector by a scalar value
    it does this by multiplying each value in the vector by the scalar value.
    
    Args:
        A vector representing a list of numbers and one scalar number.
    Returns:
        A vector where each of the values has been multiplied by the scalar.
    """
    result = [0] * len(vectora)
    for i in range (len(vectora)):
        result[i] = vectora[i] * scalarb
    return result
    
def normalize(vectora):
#calculates the normal vector
#1.) we are given a vector
#2.) we want a normal vector
#3.) we divide the vector by its norm.
    result = 0    
    if vectora == 0:
        print ("invalid input")
    elif vectora == 1:
        return vectora
    else:
        norm = twonorm(vectora)
#replace this with scalar_vector_multi(vectora)
        vectora = scalarvectormult(vectora, (1/norm))
    return vectora

print(normalize(a))
