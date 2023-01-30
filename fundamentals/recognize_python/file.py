num1 = 42  # variable declaration, data type = number (int)
num2 = 2.3  # variable declaration, data type = number (float)
boolean = True  # variable declaration, primitive data type, boolean
string = 'Hello World' # primitive data type, strings, variable declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # composite data type, list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #composite data type - dictionary
fruit = ('blueberry', 'strawberry', 'banana') # composite data type - tuple
print(type(fruit)) # type check
print(pizza_toppings[1]) # data type - composite - list - access value
pizza_toppings.append('Mushrooms') # data type - composite - list - add value
print(person['name']) # data type - composite - dictionary - access value
person['name'] = 'George' # data type - composite - dictionary - change value
person['eye_color'] = 'blue' # data type - composite - dictionary - add value
print(fruit[2]) # data type - composite - list - access and initialize

if num1 > 45: # conditional - if
    print("It's greater") # log statement
else: # conditional - else
    print("It's lower") # log statement

if len(string) < 5: # conditional - if &  length check
    print("It's a short word!") # log statement
elif len(string) > 15: # conditional - elif &  length check
    print("It's a long word!") # log statement
else: # conditional - else
    print("Just right!") # log statement

for x in range(5): # for loop start and stop
    print(x) # log statement
for x in range(2,5): # for loop start and stop
    print(x) # log statement
for x in range(2,10,3): # for loop start and stop
    print(x) # log statement
x = 0 # variable declaration
while(x < 5): # while loop start and stop
    print(x) # log statement
    x += 1 # increment

pizza_toppings.pop() # list - delete value
pizza_toppings.pop(1) # list - delete value

print(person) # log statement
person.pop('eye_color') #dictionary - delete value
print(person) # log value

for topping in pizza_toppings: # for loop start
    if topping == 'Pepperoni': # conditional if
        continue #for loop-continue
    print('After 1st if statement') # log statement
    if topping == 'Olives': #conditional if
        break # for loop-break

def print_hello_ten_times(): #function
    for num in range(10): #for loop
        print('Hello') # log statement

print_hello_ten_times() # log statement

def print_hello_x_times(x): #function and parameter
    for num in range(x): # for loop and parameter
        print('Hello') # log statement

print_hello_x_times(4) # log statement and parameter

def print_hello_x_or_ten_times(x = 10): #function and argument
    for num in range(x): # for loop
        print('Hello') # log statement

print_hello_x_or_ten_times() # log statement
print_hello_x_or_ten_times(4) # log statement and parameter


"""
Bonus section
"""

# print(num3) # NameError: name<variable name> is not defined
# num3 = 72 # variable declaration
# fruit[0] = 'cranberry' #TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) # KeyError: 'favorite_team'
# print(pizza_toppings[7]) #IndexError: list index out of range
#   print(boolean) # IndentationError: unexpected indent
# fruit.append('raspberry') # Attribute Error: 'tuple' object has no attribute 'append'
# fruit.pop(1) # Attribute Error: 'tuple' object has no attribute 'pop'