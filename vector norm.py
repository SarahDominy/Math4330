a = [1, 2, 3]
def vectorNorm(vectora):
#calculates the 2-norm of a vector
#1.) we are given a vector
#2.) we want a scalar
#3.) we add all the elements of the vector squared and then take the square root.
    result = 0
    for i in range (0,len(vectora)):
        result = result + vectora[i] ** 2
    result = result ** (1/2)
    print (result)
vectorNorm(a)
