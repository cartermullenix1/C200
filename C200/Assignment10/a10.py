import sqlite3

connection = sqlite3.connect("/mydatabase.db")
my_cursor = connection.cursor()

# Don't change the following line. This line takes care of the fact that if the table already exists then it will be 
# removed before you create it again so that you can run your program multiple times without having to manually 
# delete the table.
my_cursor.execute('''DROP TABLE IF EXISTS Pizza''')

def createTable(cursor, tableName, columns):
    query = f"DROP TABLE IF EXISTS {tableName}"
    cursor.execute(query)
    
    query = f"CREATE TABLE {tableName} ({columns})"
    cursor.execute(query)

# Create a table called Pizza with the same fields as shwon in the HW PDF, and insert data into the table
# Put data into the table fields

# Your code goes here
def insertValues(cursor, tableName, valueString):
    query = f"INSERT INTO {tableName} VALUES ({valueString})"
    cursor.execute(query)

table_name = "Pizza"

table_column = "Name TEXT, Size TEXT, Toppings FLOAT, Beverage FLOAT, Cost FLOAT"

Table_data = [
    '"Mother Bears", "large", 3.0, 2.0, 20.0', 
    '"Dominos", "small", 1.0, 3.0, 12.0',
    '"Pizza Hut", "large", 3.0, 2.0, 22.0',
    '"Toppers", "medium", 2.0, 1.0, 15.0',
    '"Avers", "large", 2.0, 3.0, 24.0',
    '"Lennys", "medium", 3.0, 4.0, 27.0',
]

createTable(my_cursor, table_name, table_column)
connection.commit()

for values in Table_data:
        insertValues(my_cursor, table_name, values)
connection.commit()
        
def queryStatement(theSelect, theFrom, theWhere=""):
    query = f"SELECT {theSelect} FROM {theFrom}"
    if theWhere != "":
        query += f" WHERE {theWhere}"
    return query

### A list is created below to help you match your SQL query output with the expected output.
data = [
    ('Mother Bears', 'large', 3.0, 2.0, 20.0),('Dominos', 'small', 1.0, 3.0, 12.0),
    ('Pizza hut', 'large', 3.0, 2.0, 22.0), ('Toppers', 'medium', 2.0, 1.0, 15.0),
    ('Avers', 'large', 2.0, 3.0, 24.0), ('Lennys', 'medium', 3.0, 4.0, 27.0)
]


# QUERY 1 Select all the pizza places
def func1(db_cursor):
    temp = []
    for i in db_cursor.execute("SELECT * FROM Pizza"):
        temp.append(i)
    return temp

# # QUERY 2 
# Select all pizza options that cost less that $20.00
def func2(db_cursor):
    temp = []
    for i in db_cursor.execute("SELECT * FROM Pizza WHERE Cost<20 "):
        temp.append(i)
    return temp


# # QUERY 3 
# Select all pizza places where toppings cost more than the toppings at Domino's
def func3(db_cursor):
    temp = []
    for i in db_cursor.execute("SELECT Name FROM Pizza WHERE Toppings > (SELECT Toppings FROM Pizza WHERE Name = 'Dominos')"):
        temp.append(i)
    return temp


# # QUERY 4 
# Select the pizza place and beverage with the highest cost 
def func4(db_cursor):
    temp = []
    for i in db_cursor.execute("SELECT Name, Beverage FROM Pizza WHERE Cost = (SELECT MAX(Cost) FROM Pizza)"):
        temp.append(i)
    return temp


# # QUERY 5 
# Select the Pizza place and Cost with the smallest number of toppings 
def func5(db_cursor):
    temp = []
    for i in db_cursor.execute("SELECT Name, Cost FROM Pizza WHERE Toppings = (SELECT MIN(Toppings) FROM Pizza)"):
        temp.append(i)
    return temp


# # QUERY 6 
# Display the average number of Toppings and Beverages
# You are not allowed to use Avg() or numpy average
# HINT: Average is the ratio of sum / number of counts, so which SQL function would give you the sum and count of entries?
def func6(db_cursor):
    temp = []
    for i in db_cursor.execute("SELECT (SUM(Toppings))/COUNT(), SUM(Beverage)*1.0/COUNT() FROM Pizza"):
        temp.append(i)
    return temp


# # QUERY 7 
# Give the counts of Pizza places by their number of Toppings
def func7(db_cursor):
    temp = []
    for i in db_cursor.execute("SELECT Toppings,COUNT(Name) FROM Pizza GROUP BY Toppings"):
        temp.append(i)
    return temp
        


if __name__=="__main__":

    # We have already completed the equivalent list comprehesnion, 
    # You should complete the functions using SQL queries to return the desired results

    print("Query 1")
    for i in func1(my_cursor):
        print(i)
    print("List Comprehension: ", data)

    print("\nQuery 2")
    for i in func2(my_cursor):
        print(i)
    print("List Comprehension: ", [d for d in data if d[4] < 20 ])

    print("\nQuery 3")
    for i in func3(my_cursor):
        print(i)
    print("List Comprehension: ",[d[0] for d in data if d[2] > [d[2] for d in data if d[0] == 'Dominos'][0]])

    print("\nQuery 4")
    for i in func4(my_cursor):
        print(i)
    print("List Comprehension: ",[(d[0],d[3]) for d in data if d[4] in (sorted(data, key = lambda x:x[4], reverse=True)[0])])

    print("\nQuery 5")
    for i in func5(my_cursor):
        print(i)
    print("List Comprehension: ",[(d[0], d[4]) for d in data if d[0] in (sorted(data, key = lambda x:x[2])[0])])

    print("\nQuery 6")
    for i in func6(my_cursor):
        print(i)
    print("List Comprehension: ", [(sum([d[2] for d in data])/len(data),sum([d[3] for d in data])/len(data))])

    print("\nQuery 7")
    for i in func7(my_cursor):
        print(i)
    print("List Comprehension: ", [(i, list(map((lambda x: x[2]),data)).count(i)) for i in set(map((lambda x: x[2]),data))])

connection.close()