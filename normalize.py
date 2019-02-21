a = [1, 2, 3]
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
#replace this with vectorNorm(vectora)
        for i in range (0,len(vectora)):
            result = result + vectora[i] ** 2
        result = result ** (1/2)
#replace this with scalar_vector_multi(vectora)
        for i in range (0,len(vectora)):
            vectora[i] = vectora[i]/result
    return vectora

print(normalize(a))
