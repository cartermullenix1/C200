"""
One of the code implementations for the problems in Lab3.py

"""

# List Operations

def manual_append(list_one, element):
    '''
    given a list and an element append the element to the list 
    note to do this operation you can't use the .append method for lists

    inputs:
    list_one - a list of values can be any type
    element - a value of any type

    output:
    one coherent list of all elements combined

    '''
    list_one = list_one + [element]
    return list_one

def manual_remove(list_one, indexToRemove):
    '''
    Give manual_remove a list of elements and choose a specific index to remove by using a for loop.

    Args: 
        list_one: the list that you are giving the function
        indexToRemove: index to be removed
    Returns:
        outputList: returns a list of values with the index removed
        eg: if list_one is [1,2,3] and index is 1. Your function would remove 2 and return [1,3]
    '''
    new_list = []
    for i in range(len(list_one)):
        if i != indexToRemove:
            new_list = manual_append(new_list, list_one[i])
    return new_list

    # new_list = list_one [:indexToRemove] + list_one [indexToRemove+1:]

    # return new_list

# Doing things with list data structures

def compare_lists(list_one, list_two):

    '''
    Given two lists compare the first one to the second one and report which numbers are different in the second list.

    Args: 
        list_one: first list
        list_two: second list
    
    Returns:
        output: list of items that were different in the second list
        eg: If you have [1,2,3,4] as list_one and [1,5,3,7] in the second list, you would return [5,7].
    '''
    different = []
    for i in range(len(list_two)):
        if list_one[i] == list_two[i]:
            pass
        else:
            different = manual_append(different, list_two[i])
    return different
        

def factorial_for(n):
    '''
    given a number calculate the factorial value using a for loop

    input:
    n - integer value that will be factorial you want to calculate 

    output:
    the calculated factorial of the input value 
    '''
    fact = 1
    for i in range(2,n+1):
        fact = fact * i
    
    """
    range (5) = (0,1,2,3,4)
    """
    return fact


if __name__ == '__main__':
    # TODO:
    # implement testing
    print(manual_append([1, 2, 3, 4, 5], 2)) # output should be true, 1
    print(manual_remove([1, 2, 7, 10, 11, 12, 3], 3))
    print(compare_lists([1,2,3,4],[1,5,3,7]))
    
    # Call the function and pass a value for n
    x = 5
    result = factorial_for(x)
    print("The factorial of", x, "is", result)
    

    pass

