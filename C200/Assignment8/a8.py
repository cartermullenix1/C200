# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np
# import math

#problem 1
def cost_2(x):
    return 2000 + (500*x)

def revenue(x):
    return (2000*x) - (10*(x**2))

def profit(x):
    return revenue(x) - cost_2(x)

def f(x):
    return (x**6 - x - 1)


#default h = 0.00001
# fp is better done with lambda (but you can implement it anyway you like)
# INPUT a function
# RETURN the derivative of input function
def fp(f, h = 0.00001):
    return lambda x:(f(x + h)-f(x-h))/(2*h)

# INPUT a function, function derivative, value of x, tau
# RETURN root
def newton(f, fp, x, tau):
    while f(x) > tau:
        x = x-(f(x)/fp(x))
    return x
        

#problem 2
#INPUT a number
#RETURN -1 if number is <= 0, 1 otherwise
def sign(x):
    while x:
        if x > 0:
            return 1
        else:
            return -1

#INPUT function, interval(a, b), tau
#RETURN root
def bisect(f,a,b,tau = .00001):
    c = (a+b)/2
    if b-c <= tau:
        return c
    else:
        if sign(f(b))*sign(f(c)) <= 0:
            a = c
            return bisect(f,a,b)
        else:
            b = c
            return bisect(f,a,b)
        
    

#problem 3
#INPUT two starting values (x0 and x1), a function and tau
#RETURN root
def secant(x0,x1,f,tau = .00001):
    while abs(f(x0)) > tau:
        old_x0 = x0
        x0 = x1
        x1 = x1 - (f(x1) * ((x1-old_x0)/(f(x1)-f(old_x0))))
    return x1
        


# problem 4
#The following function even() is given as a helper, you are free to use or not use it (as you see fit)
def even(x):
    if x % 2 == 0:
        return True

#INPUT function, start a, end b, divisions
#RETURN area
def simpson(fn,a,b,n):
    delta_x = (b-a)/n
    interval = lambda i: a + i * delta_x
    modified_delta_x = (b-a)/(3*n)
    temp = [(2 if even(i) else 4)*fn(interval(i))for i in range(1,n)]
    temp = [fn(interval(0))] + temp + [fn(interval(n))]
    return modified_delta_x*sum(temp)
    


#problem 5

# ! Important !

# To test the code on this problem, You may not run it directly in VSC (due to File not found error), 
# please follow the instructions below.

# 1. Open a new Terminal in VSC. 

# Run the below command in the terminal i.e. after typing in the command, hit enter
# 2. cd Assignment8

# Now run the a8.py in the newly opened terminal i.e. type the below command and hit enter
# 3. python3 a8.py

# It should print output on the terminal based on how much of the problem have you completed. Using this way
# of running, you can easily monitor your progress on this problem.

#the dictionary for the transation
aa_d = {}
#the FASTA file
DNA_d = []

#the correct translation
actual = "PLHSPHPANFCVFSRD-IPYSEHLRRGALDPGRFRGPRSELSEIERARSRDLRRGPGPPGGEAAARRPLEAAGPLAGPRRRSGVAGRGGFQRGDGAVRGGPGAGARPVEEAGQQRRRLHDRGPGKVRQAGRPRPQGPSLPKPPGRASPTFLSQDLPGFPRHEDLLLPPGPEPRLLTSQSPRPEGGGRAEPRRGAPGRPTPRAVRAEPPARVPAASGPGQLPGERLPCWAPVPGRAPAGWVRGACGAGAGE-ALSARRSSWATACW-PSPGTTPETSAPRCRRRWTSS-ATLSRRWFPSTAELWVGGRGIPRRPSPCLSKASPRSSLLAVLSRGQDARGRR"

#INPUT name of amino acid file (make sure that you keep the amino_acids.txt under Assignment8 folder)
#RETURN a dictionary 
#Key is a tuple (c0, c1, ... , cn) where ci are codons
#Value is a pair [name, abbreviation] for the amino acid
#make sure to close the file after reading it
def get_amino_acids(name):
    codons = []
    amino_acids = []
    with open(name,"r") as aa:
        contents = aa.read()
        # print(contents)
        contentslist = contents.splitlines()
        # print(contentslist)
        for line in contentslist:
            lists_of_line = line.split(",")
            # print(lists_of_line)
            amino_acids = lists_of_line[0:2]
            codons = lists_of_line[2:]
            codons = tuple(codons)
            aa_d[codons] = amino_acids     
    return aa_d
        

#INPUT file name of the DNA file (make sure that you keep the DNA.txt under Assignment8 folder)
#RETURN a list [header, DNA]
#header is first line in the file
#DNA is a string of letters from remainder of file
#no whitespace
#make sure to close the file
def get_DNA(name):
    with open(name,"r") as dna:
        extra = dna.readlines()
        first_part = extra[0]
        fixed = first_part.strip("\n")
        second_part = extra[1]
        total = [fixed, second_part]
        DNA_d = total
    return DNA_d
        
        

#INPUT FAST file
#RETURN a string representing the protein (convert the DNA to amino acids)
#using the dictionary
def translate(DNA_d):
    another_list = []
    important = DNA_d[1]
    for letter in range(len(important)):
        new_set = important[letter: letter+3]
        new_set_list = [new_set]
        for line in new_set_list:
            another_list.append(line)
    return another_list
    # for item in another_list:
    #     for k in aa_d.keys():
    #         for i in k:
    #             if i == item:
    #                 final_list[item].append(aa_d[k[1]])
    # print (final_list)
                
            
            

#problem 6
#cost = lambda x: ...
# INPUT: cost function
# Output marginal cost
cost = lambda x: 0.0001*(x**3) - 0.08*(x**2) + 40*x + 5000
def marginal_cost(cost):
    derrivative_cost = fp(cost)
    return derrivative_cost


if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a7.py`. Feel free to add print statements. 
    """
    # #problem 1
    # #find the root
    # print(f"f(2) = {f(2)}")
    # print(f"f(1) = {f(1)}")
    # root  = newton(f, fp(f), 2, 0.0001)
    # print(f"f({root}) = {f(root)} ~ {round(f(root),2)}")

    # # #find the maximal profit
    # m = fp(profit)
    # x = newton(m, fp(m), 1, .0001)
    # print(f"x = {x}")
    # print("The maximum profit is about ${0}".format(profit(round(x, 0))))

    # t = np.arange(0.0, 100.0)
    # fig,ax = plt.subplots()

    # ax.plot(t, profit(t),'g')
    # ax.plot(75,profit(75), 'bo--')
    # ax.set(xlabel ="Widgets Sold", ylabel="Profit ($)",
    # title = "Maximal Profit = ${0}".format(profit(75)))
    # ax.grid()
    # plt.show()

    #problem 2
    # x = bisect(lambda x: x**6 - x - 1,1.0,2.0)
    # print(f"f({x}) = {f(x)} ~ {round(f(x),4)}")

    #problem 3
    # x0,x1 = 1,2
    # f = lambda x: x**6 - x - 1
    # print(f(x0),f(x1))
    # x = secant(x0,x1,f)
    # print(f"f({x}) = {f(x)} ~ {round(f(x),4)}")
    
    #problem 4
    
    # data = [[lambda x:3*(x**2)+1, 0,6,2],[lambda x:x**2,0,5,6],
    #     [lambda x:math.sin(x), 0,math.pi, 4],[lambda x:1/x, 1, 11, 6]]


    # for d in data:
    #     f,a,b,n = d
    #     print(simpson(f,a,b,n))

    # area = simpson(lambda t: 3*(t**2) + 1,0,6,10)
    # t = np.arange(0.0, 10.0,.1)
    # fig,ax = plt.subplots()
    # s = np.arange(0,6.1,.1)
    # ax.plot(t, (lambda t: 3*(t**2) + 1)(t),'g')
    # plt.fill_between(s,(lambda t: 3*(t**2) + 1)(s)) 
    # ax.grid()
    # ax.set(xlabel ="x", ylabel=r"$f(x)=3x^2 + 1$",
    # title = r"Area under the curve $\int_0^6\,f(x)$ ~" + f"{round(area,2)}")
    # plt.show()

    #problem 5
    # You should keep the "DNA.txt" and "amino_acids.txt" files under the Assignment8 directory.
    # Also see the instructions given in comments before problem-5 code above to see the alternative way of running the program.
    # path = "Assignment8/"
    # fn1, fn2 = "amino_acids.txt", "dna.txt"
    # aa_d = get_amino_acids(path+fn1)
    # DNA_d = get_DNA(path+fn2)
    # protein = translate(DNA_d)

    # # print("Dictionary")
    # print(aa_d)
    # print("FASTA file")
    # print(DNA_d)
    # print("Translations match:", str(protein == actual))

    # #should return "PLHS"    
    # print(translate(["nothing", "CCACTGCACTCA"]))

    # #should returns "D-"
    # print(translate(["nothing", "GACTAA"]))

    #problem 6
    # U,C = [],[]
    # for unit in range(200,650,50):
    #     U.append(unit)
    #     mc = round(marginal_cost(cost)(unit),0)
    #     C.append(mc)
    #     print(f"For {unit} marginal cost is {mc}")
        
    # plt.plot(U,C,'b-')
    # plt.plot(300,round(marginal_cost(cost)(300)),'ro')
    # plt.xlabel("Units of Production")
    # plt.ylabel("Cost $")
    # plt.title(r"Marginal cost Cost(x) =  $0.0001x^3 - 0.08x^2 + 40x + 5000$")
    # plt.show()
