# from emoji import emojize
# print(emojize(":thumbs_up:"))

# range1 = list(range(1,10,2))

# print(range1)

# Prints [1,3,5,7,9]

# range2 = list(range(20,2))

# print(range2)

# Nothing [] will print due to there not being a defined starting or end point

# range3 = list(range(20,2,-2))

# print(range3)

# Prints [20,18,16,14,12,10,8,6,4]

#For
# lists = [11,12,34,50]
# for i in lists:
#     print (i)

# for i in range(len(lists)):
#     print("Index",i)
#     print("Element",lists[i])

# lists2 = [[0,1,2],['a','b','c'],[11,22,33]]
# for i in lists2:  # outer list
#     for j in i:  # elements/lists in outer list
#         print(j)

# animal_list = ['dog','cat','horse']
# for i in range(len(animal_list)):
#     print("The", str(i+1), "animal is", animal_list[i])

# list_ex = [[1,2,3], "abc", [2,3,4]]

# for i in list_ex:
#     if type(i)==list:
#         print(i)

# While

# for i in range(5):
#     print(i)

# j=0
# while j<5:
#     print(j)
#     j += 1

# # j=0
# while i<5:
#     print(i)
#     i += 1

# for j in range(5):
#     if j!=2:
#         print(j)

# j=0
# while j<5:
#     if j!=2:
#         print(j)
#     j+=1

# password = ""
# i=0
# lst = ['p','a','s','s','w','o','r','d','a','b','c']
# while password!='password':
#     password+=lst[i]
#     i+=1

# print(password)

# for i in range(5):
#     if i==3:
#         break
#     print(i)

# for i in range(5):
#     if i==3:
#         break
#     print(i)
# print ('out of loop')

# for i in range(5):
#     if i==3:
#         continue
#     print(i)

for i in range(10):

    if i%2==0:
        continue
    print(i)
    