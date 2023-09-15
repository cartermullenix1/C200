# Binary Search

# Looking for: 4
[3,4,5,6,7,8,9]

# Linear search complexity: O(n)
# Binary search complexity: O(log2(n))

# Iterative Approach
def iterativebinarySearch(array, x, low, high):
    while low <= high:
        
        mid = low + (high - low)//2
        
        if array[mid] == x:
            return mid
        
        elif array[mid] < x:
            low = mid + 1
        
        else:
            high = mid - 1
    
    return -1

# Recursive Approach

def recursivebinarySearch(array, x, low, high):
    if high >= low:
        
        mid = low + (high - low)//2
        
        if array[mid] == x:
            return mid
        
        elif array[mid] > x:
            return recursivebinarySearch(array, x, low, mid-1)
        
        else:
            return recursivebinarySearch(array, x, mid+1, high)
    else:
       return -1


example = [1,3,5,6,7,8,9]
to_find = 3

# Iteration
result = iterativebinarySearch(example, to_find, 0, len(example)-1)

if result != -1:
    print(f"Search found element {to_find} at index: {result}")

else:
    print("Element not found")

# Recursion
recursionresult = recursivebinarySearch(example, to_find, 0, len(example)-1)

if recursionresult != -1:
    print(f"Search found element {to_find} at index: {recursionresult}")

else:
    print("Element not found")
  
# Bubble Search
  
# Iteration Approach 
def iterationbubblesort(array):
    for i in range(len(array)):
        for j in range(0, len(array)-i-1):
            if array [j]>array[j+1]:
                
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

data = [-2,20,13,-5,25]

iterationbubblesort(data)

print("Sorted array:", data)


# Insertion Sort

def insertionsort(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i-1
        
        while j >= 0 and key < array[j]:
            array[j+1] =  array[j]
            j = j-1
        
        array[j+1] = key

data = [3,1,16,11,8,26,20]

insertionsort(data)

print("Sorted array:", data)