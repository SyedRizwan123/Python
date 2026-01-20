"""A function in Python is a block of reusable code that performs a specific task.
Instead of writing the same code again and again, you can put it inside a function and call it whenever needed."""

"""def my_name():
    print("Hello Vignan")
    print("Welcome")

my_name()
my_name()"""


#Passing parameter to functions
"""def my_fun2(name):
    print("Hello",name)

my_fun2("Syed")
my_fun2("John")
my_fun2("Hari")"""

#passing the multiple parameters

"""def print_coordinate(x,y):
    print('Coordinates are (',x,',',y,')')
print_coordinate(5,8)"""

"""def addition(a,b):
    print(a+b)

def sub(a,b):
    print(b-a)

def multi(a,b):
    print(a*b)

addition(5,6)
sub(6,10)
multi(5,2)"""

#in order
"""def print_coordinate(y=8, x=5):
    print('Coordinates  (',x,',',y,')')  
print_coordinate(10,6)"""

#skipping parameter values
"""def print_coordinate(x,y=0):
    print('Coordinates are(',x,',',y,')')
print_coordinate(5)"""

#def print_coordinate(x=-1,y=0):
#   print('Coordinates are(',x,',',y,')')
#print_coordinate(5,6)
#print_coordinate(5)
#print_coordinate()
#print_coordinate(y=5)

#Returning values:
"""def isEven(x):
    print("checking whether number is even or not")
    if x%2==0:
        return True
    else:
        return False
print('2 is even:', isEven(2))
print('3 is even:', isEven(3))"""

"""def addition(a,b):
    return a+b

result = addition(2,3)
print(result)"""

#Returning multiple values:unlike several other languages python allows you to return multiple values
"""def squareandcube(x):
    return x*x, x*x*x
print(squareandcube(5))"""

"""def squareandcube(x):
    return x*x, x*x*x
x2,x3=squareandcube(3)         #this is packing and unpacking concepts
print('3 square is', x2)
print('3 cube is',x3)"""


#lambda: By using lambda function, we can define this function in a single line 
"""def square(x):
    return x*x #previously we defined a function like this
print(square(3))"""

#By using lambda
"""square = lambda x:x*x
print('lambda',square(3))"""

"""add = lambda a,b:a+b 
print(add(3,8))"""


"""def process3(fun):
    print(fun(3))
process3(lambda x:x*x)
process3(lambda x:x*x*x)"""


#Calculator App
# Function for addition
"""def add(a, b):
    return a + b
# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def menu():
    print("\n----- Simple Calculator -----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

#repeats the block as long as the condition is True.
#the condition is always True, meaning the loop will run forever (infinite loop) until you manually stop it with a break statement.
while True:  #to keep showing the calculator menu continuously until the user types '5' (Exit option).
    menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting Calculator... Goodbye!")
        break

    # Get input numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform operation based on choice
    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice! Please try again.")"""


"""What is a Recursion Function?
A recursive function is a function that calls itself directly or indirectly to solve a problem. 
It repeatedly solves a smaller part of the problem until it reaches a condition called the base case, 
which stops further recursive calls

# this should be at least one if statement used to terminate the recursive function.
# it doesn't contain any looping statements."""

"""How it works:
The function calls itself repeatedly until it reaches the base case.
Each call waits for the next call to finish before returning a result."""
"""def robo():
    print('Hello')
    robo()

print(robo())"""

#controll the program 
def robo(count):
    #We must give it a base condition — a condition where it stops calling itself.
    if count == 0:           # base condition — stop when count becomes 0
        return
    print("Hello")
    robo(count - 1)          # recursive call, reducing count by 1

robo(5)