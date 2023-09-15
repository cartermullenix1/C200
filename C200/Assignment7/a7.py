import math
# import matplotlib
import numpy as np
import random as rn
import csv
# import matplotlib.pyplot as plt

#problem 1
#recursive functions

def p(n):
    if n:
        return p(n-1) + 0.02*p(n-1)
    else:
        return 10000

#MUST be implemented with tail recursion
def p_t(n, acc=10000):
    if n:
        return p_t(n-1, 0.02 * acc + acc)
    else:
        return acc

#MUST be implemented with a WHILE LOOP
def p_w(n, acc=10000):
    while n:
        acc = 0.02 * acc + acc
        n = n-1
    return acc

#MUST be implemented with generator
def p_g():
    acc,n= 10000,0
    while True:
       yield acc
       n = n-1
       acc = 0.02 * acc + acc

def c(n):
    if n > 1:
        return 9*c(n-1) + 10**(n-1) - c(n-1)
    else:
        return 9

#MUST be implemented with tail recursion
def c_t(n, acc1=9, acc2=0):
    if n > 1:
        return c_t(n-1,9*acc1 +10**(acc2+1) - acc1, acc2+1)
    else:
        return acc1
        
#MUST be implemented with a WHILE LOOP
def c_w(n, acc1=9, acc2=0):
    while n >1:
        acc1 = 9*acc1 + 10**(acc2+1) - acc1
        acc2 = acc2 + 1
        n = n-1
    return acc1

#MUST be implemented with generator
def c_g():
    acc1,acc2 = 9,0
    while True:
        yield acc1
        acc1 = 9*acc1 + 10**(acc2+1) - acc1
        acc2 = acc2 + 1     

def d(n):
    if n:
        return 3*d(n-1) + 1
    else:
        return 1

#MUST be implemented with tail recursion
def d_t(n, acc=1):
    if n:
        return d_t(n-1, 3 * acc + 1)
    else:
        return acc
        

#MUST be implemented with a WHILE LOOP 
def d_w(n, acc=1):
    while n:
        acc = 3 * acc + 1
        n = n-1
    return acc

#MUST be implemented with generator
def d_g():
    acc= 1
    while True:
       yield acc
       acc = 3 * acc + 1

#problem 2
def c_2(n, m):
    if m == 0 or n == m:
        return 1
    else:
        return c_2(n-1, m) + c_2(n-1, m-1)

def B(n):
    if n == 0:
        return 1
    else:
        return (- sum([c_2(n+1,k)*B(k) for k in range(n)]))/(n+1)


#problem 3
#input function and epsilon
#output lambda expression (derivative)
def derivative(f,epsilon):
    return lambda x:(f(x + epsilon)-f(x-epsilon))/(2*epsilon)
    
def f(x):
    return x**2 - 3*x


# problem 4
#INPUT path, file name (make sure to provide the correct path and file name). We are providing the file and you should copy it under the
#Assignment7 folder and then test the code under __main__. You need to change the path for windows system (the example given under __main__)
# assumes a Linux/MAC system. If it does not work, then please try to use the absolute path to the Assignment7 folder instead of the relative path and
# see if that solves the problem.
#OUTPUT two lists of incomes and happiness 
#from income_data.csv
def get_data(path, name):
    with open(path + name,"r") as f_in:
        header = f_in.readline()
        incomes = f_in.readlines()
        x = []
        y = []
        for income in incomes:
            newincome = income.strip("\n").split(",")
            
            x.append(float(newincome[0]))
            y.append(float(newincome[1]))
        # print(x)
        # print(y)
        return x,y
        

#INPUT two lists X values and Y values of data
#RETURN a polynomial of degree three
def make_function(X,Y,degree):
    x,y = np.array(X),np.array(Y)
    z,SSE,*_ = np.polyfit(x,y,degree,full=True)
    return np.poly1d(z),SSE

#INPUT data and model
#OUTPUT SSE
def error(X,Y,model):
    sum_ = 0
    for i in range(len(X)):
        sum_ += (Y[i]-model(X[i]))**2
    return sum_
            

#problem 5

#INPUTS ith candle (i is just the index of the sublist within the list), starting value of x, default width, and the four critical values: open, close, max\_p, min\_p.  
#RETURN three tuples: (point, width, height, color), topline, bottomline
# point is the coordinates of the lower-left point x, y, width and height are numeric values and color will be a string of color ex. 'red' or 'green'
# topline ((xt0,yt0),(xt1,yt1)) line from max to top middle of box
# bottomline ((xb0,yb0),(xb1,yb1)) line from min to bottom middle of box

# When you see the code for testing Problem5 under __main__, you will see that the first three values of the first tuple i.e., point, width and height are 
# passed as the first arguement of matplotlib.patches.Rectangle() function and the last value i.e. color is passed as the second arguement.
# Feel free to play around with the test code to get a feeling of how it is working. You will understand it much better with a bit of experimentation.

def make(i, start, width_default, d):
    top,bottom,max_p,min_p = d
    height = abs(top - bottom)
    point = (start,min(top,bottom))
    if top > bottom:
        color = "red"
    else:
        color = "green"
    x_ttl, y_ttl = int((start + (i+1) * width_default)/2), max_p
    x_tbl, y_tbl = x_ttl, max(top,bottom)
    x_btl, y_btl = int((start + (i+1) * width_default)/2), min(top,bottom)
    x_bbl, y_bbl = x_btl , min_p
    return(point,width_default,height,color),((x_ttl,y_ttl),(x_tbl,y_tbl)),((x_btl,y_btl),(x_bbl,y_bbl))

if __name__ == "__main__":
    '''please add your own tests too
    '''
    #Problem 1
    # for i,j in zip(range(5),p_g()):
    #     print(p(i),p_t(i),p_w(i),j)
    
    # # 10000 10000 10000 10000
    # # 10200.0 10200.0 10200.0 10200.0
    # # 10404.0 10404.0 10404.0 10404.0
    # # 10612.08 10612.08 10612.08 10612.08        
    # # 10824.3216 10824.3216 10824.3216 10824.3216
    
    # for i,j in zip(range(1,7),c_g()):
    #     print(c(i),c_t(i),c_w(i),j)
    
    # # 9 9 9 9
    # # 82 82 82 82
    # # 756 756 756 756
    # # 7048 7048 7048 7048
    # # 66384 66384 66384 66384
    # # 631072 631072 631072 631072
    
    
    # for i,j in zip(range(5),d_g()):
    #     print(d(i),d_t(i),d_w(i),j)
    # # 1 1 1 1
    # # 4 4 4 4
    # # 13 13 13 13
    # # 40 40 40 40
    # # 121 121 121 121

    #problem 2
    # for i in range(6):
    #     print(f"B({i}) = {B(i)}")
    # # B(0) = 1
    # # B(1) = -0.5
    # # B(2) = 0.16666666666666666
    # # B(3) = -0.0
    # # B(4) = -0.033333333333333305
    # # B(5) = -7.401486830834377e-17

    # Problem 3
    # data = 2 
    # epsilon = 10e-8
    # print((derivative(f,epsilon)(data)))
    # f_prime = derivative((lambda x:x**2-3*x),epsilon)
    # print(f_prime(data))

    # Problem 4
    # Below example is for Linux/MAC machine where the path have a / symbol in them
    # For windows, the path will have \\ symbol.
    # Revise the lab7 on files and paths for understanding the differences in the path.
    
    # path, name = "./Assignment7/", "income_data.csv"      
    # X,Y = get_data(path, name)
    # data4 = [[i,j] for i,j in zip(X,Y)]
    #print(data4) uncomment to verify data 
    # degree = 1
    # linear_model,SSE = make_function(X,Y,degree)
    # my_error = error(X,Y,linear_model)
    
    # Uncomment the rest to plot and after you are done testing-please comment the code for plotting before submitting to the Autograder. 
    # All code that is used in plotting must be commented-out before submitting to the Autograder since the Autograder can not draw plots in the browser.
    # plt.plot(X,Y,'ro')
    # xp = np.linspace(0,8,20)
    # plt.plot(xp,linear_model(xp),'b')
    # print(f"Error agrees {round(my_error,2) == round(SSE[0],2)}")
    # plt.xlabel("Income")
    # plt.ylabel("Happiness")
    # plt.legend(["data","model"])
    # plt.title(f"Happiness as a function of Income Error: {round(SSE[0],2)}")
    # plt.show()

    # After you have tested your work, please comment out the code used below for plotting before submitting to the Autograder.
    # Also comment the import matplotlib at the top of this file before submitting to Autograder.
    # Autograder can not draw graphical plots on the web so it will throw an error.

    # Problem 5
    # data5 = [[20,15,32,10],[10,14,15,9],[22,23,27,9],[15,16,16,15],[26,12,30,2],[5,30,40,4]]
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # start = 0
    # default_width = 10
    # for i in range(len(data5)):
    
    #     candle_box,top_line,bottom_line = make(i, start,default_width, data5[i])
    #     print(candle_box)
    #     ax.add_patch(matplotlib.patches.Rectangle(*candle_box[0:3],color = candle_box[3]))
    #     plt.plot([x for x,_ in top_line],[y for _,y in top_line],'black')
    #     plt.plot([x for x,_ in bottom_line],[y for _,y in bottom_line],'black')
    #     start += default_width


    # plt.xlabel("time (hour)")
    # plt.ylabel("Stock X price")
    # plt.title("Candlestick for Stock X mm/dd/yyyy")  
    # plt.xlim([0, 60])
    # plt.ylim([0, 35])
  
    # plt.show()
    