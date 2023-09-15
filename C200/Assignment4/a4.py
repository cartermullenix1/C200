import math
import random as rn

###########################################################################
# Functions for Problem 1
###########################################################################
#INPUT dlst = [day, month, year]
#RETURN string corresponding to the day of the week (i.e. "Mon", "Sun", etc)
week = {1:"Mon", 2:"Tue", 3:"Wed", 4:"Thu", 5:"Fri", 6:"Sat", 7:"Sun"}
def a(dlst):
    m = dlst[1]
    y = dlst[2]
    return y-((14-m)/12)

def b(dlst):
    x = a(dlst) + ((a(dlst))/4) - ((a(dlst))/100) + ((a(dlst))/400)
    return math.floor(x)

def c(dlst):
    m = dlst[1]
    return m+12*((14-m)/12)-2

def day(dlst):
    d = dlst[0]
    week_day = (d+b(dlst)+(31*(c(dlst)/12)))%7
    for k in week.keys():
        if k == week_day:
            return week[k]
        else:
            continue


###########################################################################
# Functions for Problem 2
###########################################################################
#INPUT t = (a,b,c)
#RETURN return complex or real roots
#CONSTRAINT round 2 places
def q(t):
    a = t[0]
    b = t[1]
    c = t[2]
    if ((b**2)-4*a*c) >= 0:
        real1 = round((-b - math.sqrt((b**2)-4*a*c))/2*a,2)
        real2 = round((-b + math.sqrt((b**2)-4*a*c))/2*a,2)
        return real1,real2
    elif ((b**2)-4*a*c) < 0:
        first_part = round(-b/2*a,2)
        second_part = complex((math.sqrt((b**2)-4*a*c)/2*a))
        complex1 = complex(first_part, second_part)
        complex2 = complex(first_part, -second_part)
        return complex(complex1), complex(complex2)
    pass


###########################################################################
# Functions for Problem 3
###########################################################################
#INPUT a nested list of people encoded as 0's and 1's. v0 and v1 are the respective lists respresenting the people pairs.
#   You'll be comparing the smallest degree of difference between each sublist representing each person.
#match() RETURN all unique pair of people with their angle
#best_match() RETURN person pair with the smallest degree (smallest degree of difference between the person pair lists)
def inner_prod(v0,v1):
    multipliedij = []
    for i in v0:
        for j in v1:
            k = i*j
            k += multipliedij
    pass

def mag(v):
    pass

#CONSTRAINT round 2 places
def angle(v0,v1):
    pass

def match(people):
    pass

def best_match(scores):
    pass 



###########################################################################
# Functions for Problem 4
###########################################################################
#INPUT tuple of quadratic (ax^2 + bx + c)
#RETURN tuple (m,n) cofficients for real solutions a(x+m)^2 + n = 0
#CONSTRAINT round 2 places
def c_s(coefficients):
    a = coefficients[0]
    b = coefficients[1]
    c = coefficients[2]
    m = round(b/(2*a),2)
    n = round(c-((b**2)/4*a),2)
    return m,n

#INPUT coefficients for quadratic ax^2 + bx + c 
#RETURN return real roots uses c_s
#CONSTRAINT round 2 places
def q_(coefficients):
    m,n = c_s(coefficients)
    root_1 = round(-m + math.sqrt(-n),2)
    root_2 = round(-m - math.sqrt(-n),2)
    return root_1,root_2

###########################################################################
# Functions for Problem 5
###########################################################################
#INPUT List of numbers
#RETURN Various means
#CONSTRAINT round 2 places
def mean(lst):
    l = len(lst)
    nmean = sum(lst)/l
    return round(nmean,2)

#CONSTRAINT round 2 places
def var(lst):
    new_lst = []
    l = len(lst)
    for i in lst:
        new_lst.append((i - mean(lst))**2)
    return round((1/(l))*sum(new_lst),2)


#CONSTRAINT round 2 places
def std(lst):
    return round(math.sqrt(var(lst)),2)

def mean_centered(lst):
    new_lst2 = []
    for i in lst:
        new_lst2.append((i - mean(lst)))
    return new_lst2



###########################################################################
# Functions for Problem 6
###########################################################################
#INPUT supply and demand coefficients
#RETURN solution of quadratic equations
def equi(s,d):
    a = s[0]
    b = s[1]
    c = s[2]
    supply_1 = (-b + math.sqrt((b**2)-4*a*c))/2*a
    supply_2 = (-b - math.sqrt((b**2)-4*a*c))/2*a
    a = d[0]
    b = d[1]
    c = d[2]
    demand_1 = (-b + math.sqrt((b**2)-4*a*c))/2*a
    demand_2 = (-b - math.sqrt((b**2)-4*a*c))/2*a
    return (supply_1, supply_2, demand_1, demand_2)


###########################################################################
# Functions for Problem 7
###########################################################################
#INPUT container, sample size n
#OUTPUT random selection of size n in any order
#CONSTRAINT: uses rn.randint(x,y) 
#Note that this is with replacement, meaning that a member from lst can be chosen more than once.
def sample(lst, n, seed1):
    
    # Don't remove the following rn.seed(seed1) line. If you remove this you might get different answers 
    # on the Auto grader and you loose marks.
    rn.seed(seed1) 
    pass
    


        



###########################################################################
# Functions for Problem 8
###########################################################################
#INPUT A string
#OUTPUT dictionary of all substrings with their size (see HW PDF)
def sub_strings(str, cnt):
    pass
    



###########################################################################
# Functions for Problem 9
###########################################################################
#INPUT values for annuity
#OUTPUT deposit amount needed
#CONSTRAINT round 2 places
def deposit(S,r,i,n):
    i = r/m
    n = m*y
    R = S/((((1+i)**n)-1)/i)
    print (R)

#INPUT sinking fund values except deposit
#OUTPUT a list of period deposit, interest, accrued total fund
#CONSTRAINT must use function deposit to determine deposit amount
#CONSTRAINT round to 2 places the value of interest and accrued amount
def sinking_fund(final_amt,r,m,y):
    pass





if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.

    You **do not** have to put anything here
    """

    # #problem 1
    # print(day([14,2,2000]))
    # print(day([14,2,1963]))
    # print(day([14,2,1972]))

    #problem 2
    # print(q((3,4,2)))
    # print(q((1,3,-4)))
    # print(q((1,-2,-4)))

    # #problem 3
    # people0 = [[0,1,1],[1,0,0],[1,1,1]]
    # print(match(people0))
    # print(best_match(match(people0)))

    # people1 = [[0,1,1,0,0,0,1],
    #            [1,1,0,1,1,1,0],
    #            [1,0,1,1,0,1,1],
    #            [1,0,0,1,1,0,0],
    #            [1,1,1,0,0,1,0]]
    # print(best_match(match(people1)))
    # # output is ([1, 1, 0, 1, 1, 1, 0], [1, 0, 0, 1, 1, 0, 0], 39.23)

    # v0,v1 = (2,3,-1), (1,-3,5)
    # print(angle(v0,v1)) #122

    # v0,v1 = (3,4,-1),(2,-1,1)
    # print(angle(v0,v1)) #85.41

    # v0,v1 = (5,-1,1),(1,1,-1)
    # print(angle(v0,v1)) #70.53


    # #problem 4 pairs should be identical
    # print(q_((6,2,1)), q_((6,2,1)))
    # print(q_((1,3,-4)),q_((1,3,-4)))
   
    
    #problem 5
    # lst = [1,3,3,2,9,10]

    # print(mean(lst))
    # print(var(lst))
    # print(std(lst))
    # print(mean(mean_centered(lst)))

    #problem 6
    s = (-.025,-.5,60)
    d = (0.02,.6,20)
    print(equi(s,d))

    #problem 7
    # lst = [1,2,1,3,4]
    # print(sample(lst, 3, 1729))
    # print(sample(lst, 3, 1629))
    # print(sample(lst, 10, 1729))

    #problem 8
    # data = ["abcabc","ccccc",""]
    # for d in data:
    #     cnt = {}
    #     sub_strings(d,cnt)
    #     print(cnt)

    #problem 9
    # S = 30000
    # m = 4
    # r = 10/100
    # y = 2
    # for i in sinking_fund(S,r,m,y):
    #     print(i)