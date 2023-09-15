import math
import random as rn
import numpy as np
# import matplotlib.pyplot as plt

########################
# PROBLEM 1
########################


#INPUT list of immutable objects
#RETURN probability distribution as a list
def makeProbability(xlst):
    entropy_dictionary = {}
    n = len(xlst)
    for element in xlst:
        if element in entropy_dictionary:
            entropy_dictionary[element] += 1
        else:
            entropy_dictionary[element] = 1
    entropy_list = []
    for item in entropy_dictionary.keys():
        t = entropy_dictionary[item]/n
        entropy_list += [t]
    return entropy_list

#INPUT probability distribution
#RETURN non-negative number entropy
def entropy(xlst):
    my_sum = 0
    problst = makeProbability(xlst)
    for item in problst:
        t = item * math.log(item,2)
        my_sum += t
    if my_sum == 0:
        return 0
    else:
        return -1 * my_sum


########################
# PROBLEM 2
########################

#INPUT list of 0s 1s
#OUTPUT longest list of 1s
def L(x):
    streak = 0
    streak_lst = []
    for i in x:
        if i == 1:
            streak += 1
        else:
            streak_lst.append(streak)
            streak = 0
    streak_lst.append(streak)
    print (streak_lst)
    highest_streak = 0
    for i in streak_lst:
        if i > highest_streak:
            highest_streak = i
        else:
            pass         
    return highest_streak



########################
# PROBLEM 3
########################
#INPUT non-negative integer
#OUTPUT True if divisible by 9, False otherwise
def div_9(x):
    current_sum = str(x)
    while len(current_sum) > 1:
        my_sum = 0
        for digit in current_sum:
            my_sum += int(digit)
        current_sum = str(my_sum)

    if current_sum == str(9):
        return True
    elif current_sum == str(0):
        return True
    else:
        return False


########################
# PROBLEM 4
########################
#INPUT string base 17 A:10, B:11,...,F:15,G:16
#OUTPUT decimal 
def secdec_dec(n):
    conver_dictionary = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16}
    power = 0
    decimal = 0
    for i in range(len(n)-1,-1,-1):
        if n[i] in conver_dictionary.keys():
            decimal += conver_dictionary[n[i]] * 17 ** power
        else:
            decimal += int(n[i]) * 17 ** power
        power += 1
    return decimal 

        

########################
# PROBLEM 5
########################
#INPUT positive number w/ two decimal places
#OUTPUT [q,d,n,p] which is the minimal number of coins
def dollars(x):
    total_cents = x * 100
    
    quarters = total_cents//25
    total_cents = total_cents % 25

    dimes = total_cents//10
    total_cents = total_cents % 10

    nickles = total_cents // 5
    total_cents = total_cents % 5

    pennies = round(total_cents,2)
    return [quarters, dimes, nickles, pennies]

########################
# PROBLEM 6
########################
#INPUT data points (x0,y0),...,(xn,yn)
#OUTPUT best regression slope m_hat, intercept b_hat
def std_linear_regression(data):
    def r(data,f):
        return sum([f(x,y) for x,y in data])
    n = len(data)
    lst = []
    xy_p = r(data, lambda x,y:x*y)
    x_s = r(data, lambda x,y:x)
    y_s = r(data,lambda x,y:y)
    x_sq = r(data,lambda x,y: x**2)
    S_xy = xy_p - ((x_s*y_s)/n)
    S_xx = x_sq - ((x_s**2)/n)
    m = round(S_xy/S_xx,2)
    b = round((y_s-(m*x_s))/n,2)
    lst += m,b
    return lst

if __name__ == "__main__":
    '''print output here '''
#     # Feel free to add your own tests here to help with error handling. 
#     print("This is the code file. To see test results, please run 'test_a5.py'")
#     print("Feel free to write your own tests here. The tests you write below will not be graded.")

    # #Problem 1
    # data1 = [["a", "b", "a", "c", "c", "a"],[1],[1,2,3,4]]
    # # 1.46, -0.0, 2.0; 0 is minimal, log(n) is maximal
    # for d in data1:
    #     print(entropy(d)) 
    # for d in data1:
    #     print(makeProbability(d)) 
 
    # #Problem  2
    # data2 = [[0],[1],[1,1,0,1,1,1],[0,1,1,0],[0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    # for d in data2:
    #     print(L(d))

    # #Problem 3
    # data3 = [99,0,18273645,22,27,274]
    # for d in data3:
    #     print(div_9(d), not bool(d % 9))

    # Problem 4
    # data4 = ["G2","100","10","GA3","G","E2"]
    # for d in data4:
    #     print(secdec_dec(d), int(d,17))
    
       
    #Problem 5
    # data5 = [2.24,1.19,4.16,1.01,1.10,2.00]
    # for i in data5:
    #       print(dollars(i))

    #Problem 6
    
    data6 = [(2,1),(5,2),(7,3),(8,3)]

    #### IMPORTANT
    ### Please comment the below code before submitting to the Autograder
    ### The Autograder can not run graohical program on Web so if you submit with the below
    ### code un-commented then it may fail the Autograder and the submission attempt may go waste.

    ### You are free to test is as many times as possible while working on the assignment but
    ### comment it before submitting.

    # m_hat, b_hat = std_linear_regression(data6)
    # print(m_hat,b_hat)
    # plt.plot([x for x,_ in data6],[y for _,y in data6],'ro')
    # plt.plot([x for x,_ in data6],[m_hat*x + b_hat for x,_ in data6],'b')
    # plt.title(r"Least Squares: $\hat{m}=0.36,\hat{b}=0.27$")
    # plt.ylabel("Y")
    # plt.xlabel("X")
    # plt.show()