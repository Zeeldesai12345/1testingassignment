def classifyTriangle(a,b,c):
    # require that the input values be >= 0 and <= 200
    
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'  
    if a <= 0 or b <= 0 or c <= 0:      # Fixed bug b=0 instead of b=b
        return 'InvalidInput'
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput'          # Fixed bug by removing ;
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):       # Fixed bug by changing a>=(b+c) or b>=(a+c) instead of a>=(b-c)) or (b>=(a-c))
        return 'NotATriangle'
    # now we know that we have a valid triangle 
    if a == b and b == c:                            # Fixed bug b==c instead of b==a
        return 'Equilateral'
    elif (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2):       # Fixed bugs by changing formula
        return 'Right'
    elif (a != b) and  (b != c) and (a != c):        # Fixed bug a != c instead of a != b
        return 'Scalene'
    else:
        return 'Isoceles'
