#this algorithm computes the conjugate of a complex number.
def conjugate (complex):
    result = 0 + 0j
    result = result + complex.real
    result = result - complex.imag*1j
    print (result)
    
