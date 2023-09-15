def factorial_iterative(n):
    factorial = 1
    for i in range(1,n+1): 
        factorial *= i    
    return factorial

print(factorial_iterative(6))