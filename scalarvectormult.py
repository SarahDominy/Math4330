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

