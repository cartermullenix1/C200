# LAMBDA Function:

def power2(n):
    return n**2

print(power2(5))

print((lambda x: x**2)(5))

summation = (lambda x,y: x+y)

print(summation(5,6))

def addtion(x,y,z):
    return x*2 + y**2 +z

print(addtion(5,6,7))

print ((lambda x,y,z: x*2 + y**2 + z)(5,6,7))

# Operators

#25/2 Quotient: 25//2 Remainder: 25%2 Division: 25/2

print(25%2)

print(25//2)

print(25/2)