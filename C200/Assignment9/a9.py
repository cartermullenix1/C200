
#no other modules can be imported
import numpy as np
# import matplotlib.pyplot as plt
import random as rn

###### Important ######
# Remember to comment out the import for matplotlib and all code for plotting before submitting to the Autograder.
# import matplotlib

import math 
from math import radians, sin, cos, sqrt, asin

# Problem 1
#translates a random integer into a step along the random walk
#parameters: int i for the step index, numpy array x for tracking the left/right location at index i,
#numpy array y for tracking the forward/backward location at index i
# A value called someVal is being passed as the 4th argument - Don't change this value. You can solve this problem without changing this value.
#return: none
def step(x,y,i, someVal):
    
    np.random.seed(someVal)

    direction = rn.randint(1, 4)
    
    # Take the step based on the randomly selected direction 
    # TODO: implement this function
    
    if direction == 1:
        x[i] = x[i-1] + 1
        y[i] = y[i-1]
    if direction == 2:
        x[i] = x[i-1] - 1
        y[i] = y[i-1]
    if direction == 3:
        x[i] = x[i-1]
        y[i] = y[i-1] + 1
    if direction == 4:
        x[i] = x[i-1]
        y[i] = y[i-1] - 1

# Do Not Modify this function. It creates the plot to show
# the random walk (as shown in the HW PDF). Once you complete
# the step() function, and run this file, you will see a plot
# similar (but not the same) to HW PDF which will show the random walk generated by your code.
# Make sure that after you are done testing, you comment the call to this function
# under the __name__ == "__main__". If you call this function and submit to the Autograder, it
# may return unexpected errors because Autograder does not support graphical plots yet.
# def graphit(x,y,n):
   
#     plt.title("Random {0} Walk\nLast Location {1},{2}".format(n,int(x[n-1]),int(y[n-1])) )
#     plt.plot(x,y) 
#     plt.plot([x[1],x[1]],[y[1]-10,y[1]+10], "b-")
#     plt.plot([x[1]-10,x[1]+10],[y[1],y[1]], "b-")
#     plt.plot([x[n-1]-10,x[n-1]+10],[y[n-1],y[n-1]], "r-")
#     plt.plot([x[n-1],x[n-1]],[y[n-1]-10,y[n-1]+10], "r-")
#     plt.show() 



# Problem 2
#INPUT class 
#RETURN complete the required functions in the class (get_numerator, get_denominator, reduce, str, add, mul)
class fraction:
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()

    def get_numerator(self):
        return self.numerator
    
    def get_denominator(self):
        return self.denominator
 
    #reduce fraction
    def reduce(self):
        def gcd(first,second):
            while second != 0:
                first,second = second,first%second
            return first
        
        temp = abs(gcd(self.denominator, self.numerator))
        while temp > 1:
            self.denominator = int(self.denominator/temp)
            self.numerator = int(self.numerator/temp)
            temp = gcd(self.numerator,self.denominator)
        return temp
    
    def __str__(self):
        return f"({self.get_numerator()}/{self.get_denominator()})"
    
    def __add__(self, other):
        numerator = (self.get_numerator()*other.get_denominator())+(other.get_numerator()*self.get_denominator())
        denominator = self.get_denominator() * other.get_denominator()
        return fraction(numerator,denominator)
        

    def __mul__(self, other):
        numerator = self.get_numerator()*other.get_numerator()
        denominator = self.get_denominator() * other.get_denominator()
        return fraction(numerator,denominator)
    

# Problem 3
# INPUT list of objects
# RETURN list of permutations
def permutation(lst):
    if len(lst) == 0:
        return [[]]
    elif len(lst) == 1:
        return [lst]
    else:
        total_perm_list = []
        for i in range(len(lst)):
            iter_list = lst[:i] + lst[i+1:]
            for j in permutation(iter_list):
                total_perm_list.append([lst[i]]+j)
                print(total_perm_list)
        return total_perm_list


# Problem 4
# Input: point p1 and p2 (points are tuples)
# Return: the distance between p1 and p2
def distance(p1, p2):
    x_1,y_1 = p1
    x_2,y_2 = p2
    distance = math.sqrt(((x_1-x_2)**2)+((y_1-y_2)**2))
    return distance
    

#Input the list containig the points (each point is a tuple)
# Return: the pair of closest points and distance in the format as shown in the PDF --> [p1, p2, distance] 
def brute(xlst):
    smallest_distance = distance(xlst[0],xlst[1])
    x = 0
    y = 0
    for i in xlst:
        for j in xlst:
            if i != j:
                if distance(i,j) < smallest_distance:
                    smallest_distance = distance(i,j)
                    x = i
                    y = j
    return [x,y,smallest_distance]


# Problem 5
    
#INPUT two tuples that have lat, lon values
#RETURN distance in miles
def hd(loc1, loc2):
    r = 3961
    lat1,lon1 = loc1
    lat2,lon2 = loc2
    new_lat1 = radians(lat1)
    new_lat2 = radians(lat2)
    dlat = radians((lat2 - lat1)/2)
    dlon = radians((lon2 - lon1)/2)
    d0 = (sin(dlat)**2) + cos(new_lat1)*cos(new_lat2)*(sin(dlon)**2)
    d1 = 2*r*asin(sqrt(d0))
    return d1

# Standard distance formula
# This is done already to help you find the answers to the question in the PDF.
# You don't have to write the answers (it's for you to investigate the differences between hd and dd)
def dd(loc1, loc2):
    """
    Standard distance formula
    """
    lat1,lon1 = loc1
    lat2,lon2 = loc2
    x = lat1 - lat2
    y = (lon1 - lon2)*cos(radians(lat2))
    return 69.385*sqrt(x**2 + y**2)

# Standard Euclidean distance
def eu_distance(loc1, loc2):    
    return sqrt(sum([(i-j)**2 for i,j in zip(loc1,loc2)]))



if __name__ == "__main__":

    '''this is the workspace'''
#     #Problem 1
#     Do not change the value of the variable someVal, others you can change and test
#     someVal = 745
#     n = 100000            # You should change the number of steps to see how it affects the plot
#     x = np.zeros(n) 
#     y = np.zeros(n) 

# #    fill array with step values 
#     for i in range(1,n):
#         step(x, y, i, someVal)

#     graphit(x,y,n)

    #problem 2
    
    # x = fraction(2*3*4,4*3*5)
    # y = fraction(2*7,-7*2)
    # z = fraction(-13,-14)
    # a = fraction(-13*2*7,14)
    # print(x,y,z,a)
    # print(f"{x} + {y} == {x + y}")
    # print(f"{x}*{y} == {x * y}")
    # b,c = fraction(1,2),fraction(3,5)
    # print(f"{b} + {c} == {b + c}")

#    Problem 3
    # print(permutation([1,2,3]))
    # print(permutation([1,2,3,4]))

    #problem 4
    # x = [(rn.randint(1,50), rn.randint(1,50)) for _ in range(10)]
    # print(x)
    # print(brute(x))

    # #problem 5
    # #Lindley Hall Home of Computer Science for decades 
    # #south side of campus
    # l1 = (39.165341,-86.523588)

    # #Luddy Hall the new Luddy building new home of Computer Science
    # l2 = (39.172725,-86.523295)

    # #Distance between Lindley and Luddy
    # print("haversine", round(hd(l1,l2),4), "mi")
    # print("Euclidean", round(eu_distance(l1,l2),4), "mi")
    # print("Approximate", round(dd(l1,l2),4), "mi")