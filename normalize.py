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
    result = result ** (1/2)
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
        for i in range (0,len(vectora)):
            vectora[i] = vectora[i]/norm
    return vectora

print(normalize(a))
