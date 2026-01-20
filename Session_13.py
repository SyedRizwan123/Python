"""def factorial(n):
    # check the base case: when n == 1 we stop the recursion
    if n == 1:
        return 1
    else:
        # recursive case:
        # return n multiplied by the factorial of (n-1)
        # this calls the same function with a smaller argument
        return n * factorial(n-1)  #it is recursive call
# call the function with n = 5 and print the result
print('Factorial of 5 is:', factorial(5))"""

"""The Fibonacci series is a sequence of numbers where:
Each number is the sum of the previous two numbers."""
"""Formula: F(n)=F(n−1)+F(n−2)
   Starting values: F(0)=0,F(1)=1"""
"""n = int(input("Enter the number of terms: "))  #10
# Initialize the first two numbers of the Fibonacci series
first = 0
second = 1
# Print the first two numbers of the Fibonacci series
print("Fibonacci Series:", first, ",", second, end=", ")
# Loop to generate and print the remaining terms of the Fibonacci series
for i in range(2, n):    #10
    # Calculate the next term in the Fibonacci series
    next_term = first + second    #0+1=1, 1+1=2 1+2=3,2+3=5, 3+5=8, 5+8=13
    #8+13=21, 13+21=34
    # Print the next term of the Fibonacci series
    print(next_term, end=", ")
    
    # Update the values of 'first' and 'second' for the next iteration
    first = second    #1``  1,2, 3,5,8,13,21
    second = next_term  #1, 2,3,5,8,13,21,34
# Print a newline character to end the output
print()"""

"""def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

terms = int(input("Enter number of terms: "))

print("Fibonacci Series:")
for i in range(terms):
    print(fibonacci(i), end=" ")"""

#Map Function
#What is map():map() applies a function to each element in a list (or iterable).
#Syntax:map(function, iterable)

# Initialize a list named 'numbers' with integers from 1 to 5.
"""numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print("Squares using map and lambda:", squares)  # Output: [1, 4, 9, 16, 25]   """

#Example 2: Convert All Strings to Uppercase
"""names = ["rizwan", "imran", "shaik"]
upper_names = list(map(str.upper, names))
print("Uppercase Names using map:", upper_names)"""  # Output: ['RIZWAN', 'IMRAN', 'SHAIK']

#Example 4: Using map() with a Defined Function
# Define a function named 'square' that takes one argument 'x'.
"""def square(x):
    return x ** 2
# Initialize a list named 'numbers' with integers from 1 to 5.
numbers = [1, 2, 3, 4, 5]
# Use the map() function to apply the 'square' function to each element in the 'numbers' list.
squared_numbers = list(map(square, numbers))
# Print the resulting list of squared numbers.
print("Squared Numbers using map and defined function:", squared_numbers)"""  # Output: [1, 4, 9, 16, 25]

#What is filter()?filter() is used to select elements that meet a condition (returns True).
#Syntax:filter(function, iterable)

#Initialize a list named 'numbers' containing a mix of integers.
# Use: This list holds the input data that will be filtered.
"""numbers = [10, 15, 20, 25, 30]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers using filter and lambda:", evens)"""  # Output: [10, 20, 30]

#Example 2: Filter Names Starting with 'A'
"""names = ["Alice", "Bob", "Anna", "Charlie", "Amanda"]
a_names = list(filter(lambda name: name.startswith('A'), names))
print("Names starting with 'A' using filter and lambda:", a_names)  # Output: ['Alice', 'Anna', 'Amanda']"""

#What is reduce()?reduce() applies a function cumulatively to all elements in a list.
#Note: It’s part of the functools module.
#Syntax:reduce(function, iterable)
"""from functools import reduce
# Initialize a list named 'numbers' with integers from 1 to 5.
# Use: This is the iterable data set on which the reduction operation will be performed.
numbers = [1, 2, 3, 4, 5]
# Use the reduce() function to cumulatively apply the lambda function to the items of 'numbers'.
# The lambda function (lambda a, b: a + b) takes two arguments:
#   'a' (the accumulator/running total) and
#   'b' (the current item from the list).
# The function returns the sum (a + b), which becomes the new 'a' in the next step.
# The result of the final cumulative addition is stored in the 'total' variable.
# 'total' will contain 1 + 2 + 3 + 4 + 5, which is 15.
total = reduce(lambda a, b: a + b, numbers)
# Print the final result of the reduction operation.
print("Total Sum using reduce and lambda:", total)"""  # Output: 15


"""The ternary operator in Python is a concise way to write an if-else statement in a single line. 
It's often used to assign a value to a variable based on a condition."""
#Syntax and Structure:value_if_true if condition else value_if_false
#Traditional if-else:
"""score = 75
if score >= 60:
    status = "Pass"
else:
    status = "Fail"
# status is "Pass" """ 

#Ternary Operator:
"""score = 75
status = "Pass" if score >= 60 else "Fail"
print(status)"""
# status is "Pass"
