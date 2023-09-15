#input radius r, height h
#return volume of cylinder

def c(r,h):
    """Input radius and height of cylinder. Returns the volume of the cylinder.

    Args:
        r (int): radius of cylinder
        h (int): height of cylinder

    Returns:
        volume (float): volume of cylinder
    """
    import math
    volume = math.pi * (r**2) * h
    return volume


def f(t):
    """Input t days. Calculates the percentage of pollutant in air after a certain amount of days of a factory running

    Args:
        t (int): days

    Returns:
        value (float): percentage of pollutant in the air
    
    """
    value = 100 * (t**2 +10*t +100) / (t**2 + 20*t + 100)
    return value


#input t hours
#return hours worked for one employee 
def P(t):
    return 0

#input x percent
#return number of seeds in an apple
def seeds(x):
    return 100

#input weight w (kg), dosage d (mg), medicine concentration mc (mg/ml)
#return Liquid Dose
# Liquid Dose = (weight*dosage)/medicine concentration
def D(w,d,mc):
    return (w*d/mc)

if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.

    You **do not** have to put anything here  """

    #volume of cylinder
    print(c(2,5)) 
    print(c(3,7))

    #pollution content
    print(f(0))
    print(f(10))

    #hours worked by an employee
    print(P(0))
    print(P(3))
    print(P(8))

    #number of seeds in an apple
    print(seeds(50))
    print(seeds(70))
    print(seeds(90))

    #liquid dose
    print(D(102,20,5))
