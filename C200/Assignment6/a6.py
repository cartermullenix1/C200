# import math
import numpy as np
# import random as rn
# import csv 
# import matplotlib.pyplot as plt

#problem 1
#recursive functions
#INPUT be watchful of inputs
#RETURN real-values
def p(n):
    if n == 0:
        return 10000
    else:
        return p(n-1) + 0.02*p(n-1)

def c(n):
    if n == 1:
        return 9
    else:
        return 9*c(n-1)+10**(n-1)-c(n-1)

def d(n):
    if n == 0:
        return 1
    else:
        return 3*d(n-1)+1

def f(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return f(n-1) + f(n-2)
    
def e(n):
    if n == 1:
        return 12
    else:
        return -5*e(n-1)

def M(c,i):
    if c == 0:
        return 1
    else:
        if c<0 or f(i)>10:
            return 0
        else:
            return M(c-f(c),i+1)+M(c,i+1)
    
def c_2(n,k):
    if k == 0 or n == k:
        return 1
    else:
        return c_2(n-1,k-1)+c_2(n-1,k)
    

#problem 2
#INPUT a list of numbers
#RETURN a triple i, j, max where the sum from i to j is max

def msi(x):
    maximum_sum = x[0]
    start_of_range = 0
    end_of_range = 0
    for i in range(len(x)):
        for j in range(i,len(x)+1):
            if sum(x[i:j]) > maximum_sum:
                start_of_range = i
                end_of_range = j
                maximum_sum = sum(x[i:j])
    return [start_of_range,end_of_range,maximum_sum]
        


# problem 3
#INPUT list of cheeses as 0, 1
#RETURN all 0s on the left, all 1s to the right
#no additional loops

def move(x):
    lo,hi = 0,len(x)-1
    while lo < hi:
        if x[lo] == 1 and x[hi] == 1:
            hi -= 1
        if x[lo] == 0 and x[hi] == 1:
            hi -= 1
            lo += 1
        if x[lo] == 1 and x[hi] == 0:
            x[hi] = 1
            x[lo] = 0
            hi -= 1
            lo += 1
        if x[lo] == 0 and x[hi] == 0:
            lo += 1    
    return x

    # Helped by Ujjwal and Anirudh in Office Hours


#problem 4
#INPUT file containing the fish data (to avoid file path problems, keep the file in the same folder as a6.py, for exmaple under the Assignment6 folder in your repo and you can direclty pass the fish_data.txt as an arguement to this function).
#RETURN two lists containing age, length as read from the file
def get_fish_data(file_name):
    with open(file_name,"r") as f_out:
        lines = f_out.readlines()
        age = []
        length = []
        for line in lines[1:]:
            nsplit = line.strip("\n").split(",")
            age.append(int(nsplit[0]))
            length.append(float(nsplit[1]))
        return age,length
        
    
#INPUT two lists X values and Y values of data
#RETURN a polynomial of degree three
def make_function(X,Y,degree):
    x_value,y_value = np.array(X),np.array(Y)
    value_polynomial = np.polyfit(x_value,y_value,degree)
    return np.poly1d(value_polynomial)
  

if __name__ == "__main__":
    '''please add your own tests too
    '''
    #Problem 1

    # p(0) = 10000
    # p(1) = 10200.0
    # p(2) = 10404.0
    # p(3) = 10612.08
    # p(4) = 10824.3216
    # print(p(4))
    
    # c(1) = 9
    # c(2) = 82
    # c(3) = 756
    # c(4) = 7048
    # c(5) = 66384   
    # print(c(2)) 

    # d(0) = 1
    # d(1) = 4
    # d(2) = 13
    # d(3) = 40
    # d(4) = 121
    # print(d(3))
    

    # f(0) = 1
    # f(1) = 1
    # f(2) = 2
    # f(3) = 3
    # f(4) = 5
    # f(5) = 8
    # print(f(4))

    # e(1) = 12
    # e(2) = -60
    # e(3) = 300
    # e(4) = -1500
    # e(5) = 7500
    # print(e(5))

    # M((0, 0)) = 1
    # M((0, 1)) = 1
    # M((0, 2)) = 1
    # M((0, 3)) = 1
    # M((0, 4)) = 1
    # M((1, 0)) = 6
    # M((1, 1)) = 5
    # M((1, 2)) = 4
    # M((1, 3)) = 3
    # M((1, 4)) = 2
    # M((2, 0)) = 6
    # M((2, 1)) = 5
    # M((2, 2)) = 4
    # M((2, 3)) = 3
    # M((2, 4)) = 2
    # M((3, 0)) = 6
    # M((3, 1)) = 5
    # M((3, 2)) = 4
    # M((3, 3)) = 3
    # M((3, 4)) = 2
    # M((4, 0)) = 0
    # M((4, 1)) = 0
    # M((4, 2)) = 0
    # M((4, 3)) = 0
    # M((4, 4)) = 0    
    # print (M(2, 2))

    # c(5,1) = 5
    # c(5,2) = 10
    # c(5,3) = 10
    # c(5,4) = 5
    # c(5,5) = 1
    # print(c_2(5,3))

    # problem 2
    # x2 = [7, -9, 5, 10, -9, 6, 9, 3, 3, 9]
    # data3 = [2,2,2,-1,-1,-1]
    # print(msi(x2))
    # print(msi(data3))
    # print("should be [0, 3, 6]")
    # data2 = [(-1)**rn.randint(0,1)*rn.randint(1,10) for _ in range(10)]
    # print(msi(x2))
    # print(data2)
    # print(msi(data2))

    # problem 3
    # data3 = [[1,0],[0,1,0,1,0,1,0],[1,1,1,1,0,0,0,0]]
    # for d in data3:
    #     result = move(d)
    #     print(f"{d} => {result}")

    # problem 4
    # name = "Assignment6/fish_data.txt"
    # X, Y = get_fish_data(name)
    # data4 = [[i,j] for i,j in zip(X,Y)]
    # print(data4)

    # After testing your program-make sure to comment out the following 
    #code (and the import for matplotlib) before submitting to the Autograder. 
    # The Autograder can not draw graphical plots in the web browser so it will return an error.

    # plt.plot(X,Y,'ro')
    # xp = np.linspace(1,14,10)
    # degree = 3
    # p3 = make_function(X,Y,degree) #model 
    # plt.plot(xp,p3(xp),'b')
    # plt.xlabel("Age (years)")
    # plt.ylabel("Length (inches)")
    # plt.title("Rock Bass Otolith")
    # plt.show()
    
    