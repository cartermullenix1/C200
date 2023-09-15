import math

#Problem 1

#INPUT n0 start colony size, m growth rate, t time
#RETURN final colony size
def N(n_0, m, t):
    size = n_0 * math.exp(m*t)
    return size

#INPUT t days
#RETURN number of teeth
def N_t(t):
    teeth = 71.8 * math.exp(-8.96*math.exp(-0.0685*t))
    return math.ceil(teeth)

#INPUT pressures Pi, Pf 
#RETURN work joules
def W(P_i, P_f):
    R = 8.314
    T = 300
    work = R*T * math.log(P_i/P_f)
    return math.ceil(work)


#INPUT V miles per hour, A area, C_l lift coefficient
#RETURN lbs 
def L(V,A,C_l):
    k = 0.0033
    lift = k * (V**2) * A * C_l
    return math.ceil(lift)

###########################################################################
# Functions for Problem 2
###########################################################################
#INPUT t = (a,b,c)
#RETURN True if discriminant is real, False otherwise
def q(t):
    a = t[0]
    b = t[1]
    c = t[2]
    discriminant = ((b**2)-(4*a*c))
    if discriminant > 0:
        return True
    else:
        return False


###########################################################################
# Functions for Problem 3
###########################################################################
#INPUT item and list
#RETURN True if item is in the list
#CONSTRAINT You cannot use 'in' -- must use bounded looping
def m(x,lst):
    for i in lst:
        for j in i:
            x = j[0]
            if x == lst:
                return True
                    
        
        

        

#INPUT nested list and list
#RETURN total amount owed (round values up to 2 nearest decimal places)
def amt(r, no_tax):
    pass

###########################################################################
# Functions for Problem 4
###########################################################################
#INPUT p0 = (x0,y0) p1 = (x1,y1)
#RETURN dictionary y = mx + b
def make_line(p0,p1):
    x0,y0,x1,y1 = *p0,*p1
    m = round((y1 - y0)/(x1 - x0),2)
    b = round(y0 - (m*x0),2)
    return {'m':m, 'b':b}

#INPUT two lines as dictionary
#RETURN a point (x,y) of intersection 
#rounded to two places
def intersection(l0,l1): 
    pass



###########################################################################
# Functions for Problem 5
###########################################################################
#INPUT List of numbers
#RETURN Various means or error message

err_msg = ["Data Error: 0 values", "Data Error: 0 in data"]

def arithmetic_mean(nlst):
    n = len(nlst)
    sum_of_lst = sum(nlst)
    mean = sum_of_lst/n
    return mean

# def geo_mean(nlst):
#     new_nlst = []
#     n = len(new_nlst)
#     for num in nlst:
#         math.log10(num)
#     return sum(new_nlst)/n

def har_mean(nlst):
    pass

def RMS_mean(nlst):
    pass


###########################################################################
# Function for Problem 6
###########################################################################
#INPUT x object, list of objects, integer y
#RETURN true if x occurs at least y times, false otherwise
def occur_at_least(x,lst,y):
    pass



###########################################################################
# Functions for Problem 7
###########################################################################

#INPUT list [p,i,n] principal, interest rate, payments
#RETURN montly payment float
def Mortgage(house):
    p = house[0]
    i = house[1]
    n = house[2]
    m = p*((((i/12)/100)*((1+((i/12)/100))**(n*12)))/((1+((i/12)/100))**(n*12)-1))
    m_round = round(m,2)
    return m_round


#INPUT list [p,i,n] principal, interest rate, payments
#RETURN the difference between total payout and value
#of home (round the answer to two decimal places)
#REQUIRES Mortgage function
def total_paid(house):
    p = house[0]
    i = house[1]
    n = house[2]
    m = p*((((i/12)/100)*((1+((i/12)/100))**(n*12)))/((1+((i/12)/100))**(n*12)-1))
    m_round = round(m,2)
    total = m_round*(n*12)-p
    return round(total,2)


###########################################################################
# Functions for Problem 8
###########################################################################
#INPUT list of numbers
#RETURN 1 if geometric series, 0 otherwise
def is_geo(xlst):
    pass

###########################################################################
# Functions for Problem 9
###########################################################################
#INPUT pair of points in 2D
#RETURN distance round to two decimal places
def net_displacement(p0,p1):
    pass

#INPUT starting position [x,y] and list of one step directions w,e,s,n that move the positon
#of x,y
#RETURN a list of starting point, distance, distance from start
def track(start_pos, movement):
    pass

###########################################################################
# Functions for Problem 10
###########################################################################
#INPUT pair of tuples from tracking
#RETURN distance betweem two ending places 
def final_distance(m0,m1):
    pass

###########################################################################
# Functions for Problem 11
###########################################################################
#INPUT conference and game
#RETURN the dictionary after updating it with the game info: change wins,losses, percentages of teams (there are no ties)
def update(conference,game):
    pass

###########################################################################
# Functions for Problem 12
###########################################################################
#INPUT amt and list of donations
#RETURN tuple: amt, donations left, the amount of the goal left
def go_fund_me(amt,donations):
    pass


if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.

    You **do not** have to put anything here
    """
    # #problem 1
    # print(N(500,100,4)) 
    # print(N_t(1000))
    # print(W(10,1))
    # print(L(33.8,512,0.515))

    #problem 2
    # print(q((1,4,-21)))
    # print(q((3,6,10)))
    # print(q((1,0,-4)))

    #problem 3
    # receipt = [[1,1.45],[3,10.00],[2,1.45],[5,2.00]]
    # no_tax = [33,5,2]
    # print(amt(receipt,no_tax))

    # #problem 4
    # p0 = (32,32)
    # p1 = (29,5)
    # p2 = (15,10)
    # p3 = (49,25)
    # p4 = (15,30)
    # p5 = (50,15)
 
    # l0,l1 = make_line(p0,p1),make_line(p2,p3)
    # print(intersection(l0,l1))
    # l0 = make_line(p4,p5)
    # print(intersection(l0,l1))
    
    #problem 5
    print(arithmetic_mean([1,2,3]))
    # print(geo_mean([2,4,8]))
    print(har_mean([1,2,3]))
    print(RMS_mean([1,3,4,5,7]))

    #problem 6
    # data6 = [[1,[1,2,1,2,1,1],4], [1,[1,2,1,2,1,1],3],
    #     [1,(1,2,1,2,1,0),4], ]

    # for d in data6:
    #     print(occur_at_least(*d))

    #problem 7
    house = [300000,2.9,30]
    print(Mortgage(house))
    print(total_paid(house))

    # #problem 8
    # xlst = [1/2,1/4,1/8,1/16,1/32]
    # print(is_geo(xlst))
    # xlst = [1,-3,9,-27]
    # print(is_geo(xlst))
    # xlst = [625,125,25]
    # print(is_geo(xlst))
    # xlst = [1/2,1/4,1/8,1/16,1/31]
    # print(is_geo(xlst))
    # xlst = [1,-3,9,-26]
    # print(is_geo(xlst))
    # xlst = [625,125,24]
    # print(is_geo(xlst))
    # print(is_geo([1/2,1/4]))

    # #problem 9
    # data_m9 = [[(0,0), list(10*'n' + 15*'e' + 10*'s'+15*'w')],
    #       [(0,0), list(3*'n' + 4*'e')],
    #       [(1,2), list(3*'s' + 4*'w')]]

    # for d in data_m9:
    #     print(track(*d))

    # #problem 10
    # data_m10 = [[(0,0), list(10*'n' + 15*'e' + 10*'s'+15*'w')],
    #       [(0,0), list(3*'n' + 4*'e')],
    #       [(1,2), list(3*'s' + 4*'w')]]

    # print(final_distance(track(*data_m10[1]),track(*(data_m10[2]))))

    # #problem 11
    # big_10_women = {'IU':{'W':12,'L':1,'PCT':.923, 'Home':(13,0)},
    #             'PU':{'W':6,'L':6,'PCT':.500, 'Home':(8,4)}, 
    #             'IOWA':{'W':11,'L':1,'PCT':.917, 'Home':(11,1)},
    #             'NW':{'W':1,'L':11,'PCT':.083,'Home':(6,6)}}
    
    # print(big_10_women['IU'],big_10_women['IOWA'])
    # update(big_10_women,{'IU':87,'IOWA':78})
    # print(big_10_women['IU'],big_10_women['IOWA'])

    # #problem 12
    # data12 = [[100,[10,15,20,30,29,13,15,40]],
    #     [100,[]],
    #     [100,[30,4]]]

    # for d in data12:
    #     print(go_fund_me(*d))