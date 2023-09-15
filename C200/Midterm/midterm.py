import math

def f(lst):
    count = {}
    for obj in lst:
        str_obj = str(obj)
        for num in str_obj:
            if num.isdigit():
                if num in count:
                    count[num] += 1
                else:
                    count[num] = 1
                if '0' not in count.keys():
                    count['0'] = 0
                if '1' not in count.keys():
                    count['1'] = 0
                if '2' not in count.keys():
                    count['2'] = 0
                if '3' not in count.keys():
                    count['3'] = 0
                if '4' not in count.keys():
                    count['4'] = 0
                if '5' not in count.keys():
                    count['5'] = 0
                if '6' not in count.keys():
                    count['6'] = 0
                if '7' not in count.keys():
                    count['7'] = 0
                if '8' not in count.keys():
                    count['8'] = 0
                if '9' not in count.keys():
                    count['9'] = 0
    if '0' not in count.keys():
        count['0'] = 0
    if '1' not in count.keys():
        count['1'] = 0
    if '2' not in count.keys():
        count['2'] = 0
    if '3' not in count.keys():
        count['3'] = 0
    if '4' not in count.keys():
        count['4'] = 0
    if '5' not in count.keys():
        count['5'] = 0
    if '6' not in count.keys():
        count['6'] = 0
    if '7' not in count.keys():
        count['7'] = 0
    if '8' not in count.keys():
        count['8'] = 0
    if '9' not in count.keys():
        count['9'] = 0
                            
    return count



def fuel_mass(mass_of_rocket, delta_v, v_e):
    wet_mass = mass_of_rocket * math.exp(delta_v/v_e)
    return math.ceil(wet_mass - mass_of_rocket)

if __name__ == "__main__":
    '''add output below this line'''
    #Problem 1
    data = [['0123456789'],[-0.1,"23",(4,5),[6,"7"],8-9j],[]]

    for d in data:
        print(f(d))
    
    #Problem 2
    delta_v = 13                 #km/sec
    v_e = 4.5                    #km/sec
    mass_of_rocket = 74843       #kg
    print(fuel_mass(mass_of_rocket,delta_v,v_e))