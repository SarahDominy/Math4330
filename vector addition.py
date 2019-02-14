#write a function for vector addition
#1. 3 questions
#2. write algorithm
#3. implement your algorithm
    #1) what do we want to do?
    # we want to add two vectors
    #2) what do we have?
    # we have two vectors
    #3) what do we want to have?
    # we want a vector that is the sum of the vectors
a = [1, 2, 3]
b = [3, 4, 5]
def vectorAddition(vectora,vectorb):
    resultant = a
    for i in range (0,len(vectora)):
        resultant[i] = vectora[i] + vectorb[i]
    print ("resultant = ", end = "")
    print (resultant)
vectorAddition(a,b)
