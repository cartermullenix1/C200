###########################################################
# factorial
###########################################################

def factorial(n):
    """
    Recursive function to calculate the factorial of n

    Input:
        n (an integer)
    Returns:
        n! = n*(n-1)*...*2*1
    """
    # Base Case
    if n == 0:
        return 1
    # Induction Step
    else:
        return n*factorial(n-1)

def tail_factorial(n, a=1):
    # a = 1 is called an accumulator
    """
    Tail-recursive function to calculate the factorial of n

    Input:
        n (an integer)
    Returns:
        n! = n*(n-1)*...*2*1
    """
    # Base Case
    if  n == 0:
        return a
    # Induction Step
    else:
        return tail_factorial(n-1,a=a*n)

d = {}
def memo_factorial(n):
    """
    Memoized function to calculate the factorial of n

    Input:
        n (an integer)
    Returns:
        n! = n*(n-1)*...*2*1
    """
    # This allows us to keep from repeating calculations for keys already in the dictionary.
    if n not in d.keys():
        # Base Case
        if n == 1:
            d[n] = 1
        # Induction Step
        else:
            d[n] = n*memo_factorial(n-1)
        
    return d[n]

###########################################################
# only_ints
###########################################################

def only_ints(xlist):
    """
    Recursive function to return a list with all non-ints taken
    out of it.

    Input:
        xlist - a list of elements
    Returns:
        xlist, but with only the 'int'-type elements kept.

    """
    # Base Case
    if not xlist:
        return []
        
    # Induction Step
    else:
        if isinstance(xlist[0], int):
            return [xlist[0]] + only_ints(xlist[1:])
        
        else:
            return only_ints(xlist[1:])
        

def tail_only_ints(xlist, a=[]):
    """
    Recursive function to return a list with all non-ints taken
    out of it.

    Input:
        xlist - a list of elements
    Returns:
        xlist, but with only the 'int'-type elements kept.

    """
    # Base Case
    if not xlist:
        return a
    # Induction Step
    else:
        if isinstance(xlist[0], int):
            return tail_only_ints(xlist[1:], a=a+[xlist[0]])
        else:
            return tail_only_ints(xlist[1:], a=a)

d = {}
def memo_only_ints(xlist):
    """
    Recursive function to return a list with all non-ints taken
    out of it.

    Input:
        xlist - a list of elements
    Returns:
        xlist, but with only the 'int'-type elements kept.

    """
    if xlist not in d.keys():
        if not xlist:
            d[xlist] = []
        
        else:
            if isinstance(xlist[0], int):
                d[xlist] = [xlist[0]] + memo_only_ints(xlist[1:])
            else:
                d[xlist] = memo_only_ints(xlist[1:])
    return d[xlist]

if __name__ == "__main__":
    # Write your own print statements here
    # to briefly test your code
    print(factorial(5))
    
    print(tail_factorial(16))
    
    print(memo_factorial(639))
    
# only_ints_test_cases = [(1.6,7,9),(78,7.6,3),(1,45,8.4)]

print(only_ints((1.6,7,9)))

print(tail_only_ints((78,7.6,3)))

print(memo_only_ints((1,45,8.4)))
    
    
    
    
    