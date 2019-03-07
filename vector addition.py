def vectorAddition(vectora,vectorb):
    """
    This algorithm calculates the sum of two vectors.

    Args:
        Two vectors, each representing a list of numbers
    Returns:
        A vector that is the sum of both vectors.
    """
    resultant = a
    for i in range (0,len(vectora)):
        resultant[i] = vectora[i] + vectorb[i]
    return resultant      
        
