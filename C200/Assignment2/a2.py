import math

#problem 1
#input real number
#return real number
def g(x):
    if x != 0:
        return x+2
    else:
        return 1



#problem 2
#input year 1977-1997
#return percent income or "error: year" if year 
#is outside range
def f(t):
    if 1977<=t<=1984:
        return (2/7)*(t-1977)+12
    elif 1984<t<=1987:
        return (t-1977)+7
    elif 1987<t<=1997:
        return (3/5)*(t-1977)+11
    else:
        return "error: year"

#problem 3
#round to 2 decimal places
#input t years = 0, 1, then 2
#output dollars
def h_0(t):
    OEM=110/((1/2)*t+1)
    return round (OEM,2)

def h_1(t):
    NONOEM=26*(((1/4)*(t**2)-1)**2)+52
    return round (NONOEM,2)

def h(t):
    HTOTAL = h_0(t) - h_1(t)
    return round (HTOTAL,2)


#problem 4
#input tuple (a,b,c) coefficients
#output tuple roots (x_1, x_2) where x_1 >= x_2
def q(coefficients):
    a = coefficients[0]
    b = coefficients[1]
    c = coefficients[2]
    d = ((b**2)-(4*a*c))
    x_1 = (-b + math.sqrt(d))/(2*a)
    x_2 = (-b - math.sqrt(d))/(2*a)
    tup = x_1, x_2
    return tup

#problem 5
#input [arg1,op,arg2,ans]
#output arg1 op arg2 == ans
def eq(lst):
    arg1,op,arg2,ans = lst
    if op == "+":
        if arg1 + arg2 == ans:
                return True
        else:
            return False
    if op == "-":
        if arg1 - arg2 == ans:
            return True
        else:
            return False
    if op == "*":
        if arg1 * arg2 == ans:
            return True
        else:
            return False
    if op == "/":
        if arg1 / arg2 == ans:
                return True
        else:
            return False

#problem 6
#input string of COVID symptoms "ABC", "ACB",...,"CBA"
#output 'very likely', 'likely', 'somewhat likely' based on severity
def covid(symptoms):
    A,B,C = symptoms
    if symptoms[0] == "A":
        return "very likely"
    elif symptoms[0] == "B":
        return "likely"
    elif symptoms[0] == "C":
        return "somewhat likely"

#problem 7
#INPUT two numbers
#RETURN maximum of the two
#You cannot use Python's max function
#You must use if, elif, else (or some combination)
def max2d(x,y):
    if x>y:
        return x
    else:
        return y

#INPUT 3 numbers
#RETURN maximum of the three
#You must use your max2D function
def max3d(x,y,z):
    if (max2d(x,y)) > z:
        return max2d(x,y)
    else:
        return z

#problem 8

line = {'slope':None, 'intercept':None}

# You don't have to change this function, we have already completed the clear_line() function for you.
# but you are welcome to see what it does.
#input line dictionary
#assigns None to both keys
#return True
def clear_line(line):
    line['slope'] = line['intercept'] = None
    return True

#input two tuples p0 = (x0,y0), p1 =(x1,y1), dictionary line
#output returns dictionary with keys assigned to slope, intercept
#unless the slope is undefined--in this case, return the dictionary
#unchanged
def build_line(p0,p1,line):
    x0,y0,x1,y1 = *p0,*p1
    line['slope'] = (y0-y1)/(x0-x1)
    line['intercept'] = y0-(((y0-y1)/(x0-x1))*x0)

#input dictionary 
#output return -(1/m) if slope is defined, otherwise return 'Error: no slope'
def inverse_slope(line):
    line['slope']
    pass

#input three tuples 
#output True if colinear, False otherwise
def colinear(p0,p1,p2):
    slope1 = (abs(p1[0]-p0[0]),abs(p1[1]-p0[1]))
    slope2 = (abs(p2[0]-p1[0]),abs(p2[1]-p1[1]))
    if slope1 == slope2:
        return True
    else:
        return False

#problem 9 
#INPUT three values: all have values or two have values and the remain has None
#OUTPUT for two values, return the computed None variable
#for three values return True or False using isclose(x,y,abs_tol = 0.001)
#remember to convert degrees to radians
def solve(theta,opposite,adjacent):
    T,O,A = theta, opposite, adjacent
    if T == None:
        return math.degrees(math.atan(O/A))
    if O == None:
        return math.tan(math.radians(T))*A
    if A == None:
        return O/math.tan(math.radians(T))
    x,y = math.tan(math.radians(T)),(O/A)
    if math.isclose(x,y,abs_tol=0.001) == True:
        return True
    else:
        return False

if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the unit testing Feel free to add print statements. 
    You should uncomment *after* you've completed the function and comment it back
    before submitting to the Autograder. 
    """

    #problem 1 
    # print(g(0))
    # print(g(1))
    # print(g(1.01))

    #problem 2
    # print(f(1976))
    # print(f(1977))
    # print(f(1985))
    # print(f(1988))
    # print(f(2000))

    #problem 3
    # print(h(0))
    # print(h(1))
    # print(h(2))

    #problem 4
    # print(q((1,0,-1)))
    # print(q((6,-1,-35)))
    # print(q((1,-7,-7)))

    #problem 5
    # print(eq([14, "/",2, 7]))
    # print(eq([20, "*",19, 381]))
    # print(eq([20, "*",19, 380]))
    # print(eq([1.1,'-',1,.1])) #saw in class this doesn't work! (will return False)

    #problem 6
    # print(covid('ABC'),covid('ACB'))
    # print(covid('BAC'),covid('BCA'))
    # print(covid('CAB'),covid('CBA'))

    #problem 7
    # print(max3d(1,2,3))
    # print(max3d(1,3,2))
    # print(max3d(3,2,1))

    #problem 8
    # print(line)
    # build_line((2,3),(8,6),line)
    # print(line)
    # clear_line(line)
    # print(line)
    # build_line((2,3),(2,5),line) #not a line
    # print(line)

    # clear_line(line)
    build_line((-3,2),(4,-1),line)
    print(line)
    print(inverse_slope(line))
    print(colinear((-2,1),(1,7),(4,13)))

    #problem 9
    # print(solve(5,None,105600))
    # print(solve(None,9238.9,105600))
    # print(solve(5,9238.8,None))
    # print(solve(5,9238.8,105600))
    # print(solve(5,9100,105600))
