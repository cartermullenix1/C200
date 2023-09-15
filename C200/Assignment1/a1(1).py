import math

# Remember, you must return from the function and not print(). print() is not the same as return.

# Usage of the round method
# a = 30.4567
# Round it to 2 decimals round(a,2) 
# For more information refer the official documentation of Python, you can also do help(round) in python shell.

# Problem 1
#input radius r, height h
#return volume and round it to 2 decimals
def c(r,h):
    volume = (1/3) * math.pi * (r**2) * h
    return round(volume,2)

# Problem 2
#input t days
#output oxygen conten percent of it normal level 
# Return the value by rounding it to 2 decimal places
# Hint declare 2 variables numerator and denominator
def f(t):
    oxygen = 100 * (((t**2)+(10*t)+100)/((t**2)+(20*t)+100))
    return round(oxygen,2)

# Problem 3
#input t hours
#return percent watching tv also round it to 2 decimal places
def P(t):
    watching = ((0.01354*(t**4))-(0.49375*(t**3))+(2.58333*(t**2))+(3.8*t)+31.60704)
    return round(watching,2)

# Problem 4
#input x percent
#return millions of dollars also round it to 2 decimal places
def cost(x):
    cost = ((0.5*x)/(100-x))
    return round(cost,2)

# Problem 5
#input dosage a mg and years t
#return child dosage mg also round it to 2 decimal places
def D(t,a):
    child = (((t+1)/24)*a)
    return round(child,2)

# Problem 6
#input number of susceptible, but healthy children
#output number of the infected children and use math.ceil()
def I(S):
   infected = ((192*(math.log2((S/762))))-S+763)
   return math.ceil(infected)

# Problem 7
#input number of items 
#output total cost 
def C(q):
    cost = ((0.01*(q**3))-(0.6*(q**2))+(13*q)+1000)
    return (cost)

#input number of items
#output average cost also round it to 2 decimal places
def A(q):
    avgcost = ((C(q))/q)
    return round(avgcost,2)

# Problem 8
#input months t=0,...,11
#output items sold x 1000 
def hh(t):
    sticks = (532)/(1+(869*math.exp(-1.33*t)))
    return math.floor(sticks)

# Problem 9
#input time seconds
#output feet also round it to 2 decimal places
def height(t):
    stone = ((-16*(t**2))+(64*t)+80)
    return round(stone,2)

# Problem 10
#input t hours
#output percent treatment also round it to 2 decimal places
def time(t):
    treatment = ((0.44*(t**4)+700)/(0.1*(t**4)+7))
    return round(treatment,2)

# Problem 11
#input coefficients for quadratic and value
#output True if value is root, False otherwise 
def quad(a,b,c,v):
    quadratic = ((a*(v**2))+(b*v)+c)
    if quadratic == 0:
        return (True)
    else:
        return (False)



if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try under
    this if statement.

    make sure that you comment the print statements 
    before submitting to the Autograder.
    """

    # volume of cone
    # print(c(2,5)) 
    # print(c(3,7))

    #oxygen content
    # print(f(0))
    # print(f(10))

    #tv watching
    # print(P(0))
    # print(P(3))
    # print(P(8))

    #x% cost
    # print(cost(50))
    # print(cost(70))
    # print(cost(90))

    #cowling's rule
    # print(D(4,500))

    # Flu Outbreak
    # print(I(200))
    # print(I(450))

    # Cost
    # print(C(15))
    # print(C(25))

    # Average Cost
    # print(A(12))
    # print(A(24))

    # sales model
    print(hh(0))
    print(hh(5))
    print(hh(10))

    # Throwing a Stone
    # print(height(4))
    # print(height(8))

    # Treating Heart Attacks
    # print(time(1))
    # print(time(2))

    # a,b,c = 2,5,-12 z = -4,3/2
    # print(quad(2,5,-12,-4))
    # print(quad(2,5,-12,3/2))
    # print(quad(2,5,-12,1))
