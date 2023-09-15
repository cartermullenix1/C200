#INPUT x number
#RETURN square of number
#this is intensionally wrong


# There would be bunch of functions like this in the 
# assignment that you'd have to complete 
# as per the instructions. For example, in the S funciton
# below, it's supposed to return the square if the input number
# but it's not doing that - so we will fix it and test it.


def S(x):
    y = 2*x
    return y

if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.

    You **do not** have to put anything here  """

    print(S(0))
    print(S(1))
    print(S(2))  