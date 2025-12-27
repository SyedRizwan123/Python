#Find the factorial number of given value
"""n = int(input("Enter any value: "))
fact = 1
i = 1
while i <= n:        # 1<=5  2<=5 3<=5  4<=5 5<=5  6<=5
    fact = fact * i          #1*1=1 fact=1 fact=1*2=2 fact=2*3=6  fact=6*4=24   fact=24*5=120
    i = i + 1

print(f"Factorial value is {fact}")"""

#Find the given is prime number or not
#prime number: Prime: if its only divisible by one and then its self     1*3=3,3*1=3   1*4=4,4*1=4,2*2=4   1*6=6,2*3=6,6*1=6   1*5=5,5*1=5                                     
"""n=int (input("Enter a number: "))
count=0    #we have to write this count after writting if statement

for i in range(1, n + 1):    #range(1, n+1): Generates a sequence of numbers from 1 to n (inclusive)
    if n % i == 0:        #3%1==0,  3%3=0
        count += 1      #coun=count+1, 0+1=1
if count == 2:
    print("Given number is a prime number")
else:
    print("Given number is not a prime number")"""

#Find the given is prime number or not
#prime number: Prime: if its only divisible by one and then its self     1*3=3,3*1=3   1*4=4,4*1=4,2*2=4   1*6=6,2*3=6,6*1=6   1*5=5,5*1=5                                     
#print the next prime number
"""prime = int(input("Enter the number: "))  #14
count = 0

# Check if the input number is prime
for i in range(1, prime + 1):
    if prime % i == 0:
        count += 1

if count == 2:
    print(prime, "is a prime number")
else:
    # If the number is not prime, find the next prime number
    prime += 1  # Start checking from the next number  #15,16
    while True:
        count = 0  # Reset count for the new number
        for i in range(1, prime + 1):
            if prime % i == 0:
                count += 1
        if count == 2:  # Check if the current number is prime
            print("The next prime number is:", prime)
            break
        prime += 1  # Move to the next number"""

# Simple Triangle Pattern

"""rows = 6 # Sets the total number of rows for the triangle pattern.
for i in range(1, rows):  # Loop from 1 to rows-1 (i = 1 to 5)
    spaces = rows - i - 1         # Calculate number of spaces before the stars for current row
    stars = 2 * i - 1             # Calculate number of stars for current row (odd numbers: 1, 3, 5, ...)
    print(" " * spaces + "*" * stars)  # Print spaces followed by stars on the same line
    # " " * spaces: adds leading spaces to center the triangle
    # "*" * stars: prints the required number of stars for the row"""

"""for i in range(1, 7):
    for j in range(1, 7):
        if j <= i:
            print("*", end=" ")
        else:
            print(" ", end="")
    print()"""

#String Concantination
"""f_name="Syed"
l_name=" Rizwan"

full_name=f_name+l_name
print(full_name)"""

#Using f-strings (Formatted String Literals):  f-strings are a concise and readable way to format strings. They allow you to embed expressions directly within string literals by using curly braces {}
"""name = "Zareena"
age = 22
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)"""

# string can be counted from the left using +ve indices, starting with 0
"""word = "python"
word1= "monthy python"
print(word[0])
print(word[1])
print(word[2])
print(word[3])        
print(word[4])
print(word[5])"""


#string can be counted from the right using -ve indices,starting with -1
"""word="python"
print(word[-1])
print(word[-2])
print(word[-3])
print(word[-4])
print(word[-5])
print(word[-6])"""

"""input_string = "Hello World!"
vowels = "aeiouAEIOU"  
vowel_count = 0
vowel_list = []

for char in input_string:
    if char in vowels:
        vowel_list.append(char)
        vowel_count += 1

print("Vowels in the given string:", vowel_list)
print(f"Number of vowels in the given string: {vowel_count}")"""

"""input_string = "Python"
reversed_string = input_string[::-1]   # Using slicing to reverse the string
print("Reversed string:", reversed_string)"""

# The loop iterates from the first character to the last
"""input_string = "Python"  # Input string to be reversed
reversed_string = ""  # Initialize an empty string to store the reversed string
# Loop through each character of the input string
# The loop iterates from the first character to the last
for char in input_string:
    reversed_string = char + reversed_string
print("Reversed string:", reversed_string)"""   # Print the final reversed string"""

#madam
# Program to check if a string is a palindrome
"""input_string="madam"
if input_string == input_string[::-1]:  # Compare the string with its reverse
    print("Palindrome")
else:
    print("Not a palindrome")"""

#print("Syed".count('e'))
# Program to find the first non-repeating character in a string 
#print("Syed".count('e'))
# Program to find the first non-repeating character in a string 
"""input_string = "aabbcde"
for char in input_string:
    if input_string.count(char) == 1:    #print("syed".count('e')) output:1
        print("First non-repeating character:", char)
        break"""

#List: List are mutable sequance, typically used to store collections of homogenious items
# Lists are represented by comma-separated items within square brackets []
"""listpeople = ["tom","harry","jane","liz"]

#Length of lists
print("length position->",len(listpeople))"""

#Find the largest and smallest element in a list without using built-in functions
"""numbers = [12, 45, 67, 2, 89, 34]
largest = numbers[0]
smallest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num
print("Largest:", largest)
print("Smallest:", smallest)"""

#Find the sum and average of list elements
"""numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
print(total)
average = total / len(numbers)
print("Sum:", total)
print("Average:", average)"""

#Searching and sorting in list
#Linear Search: Works on unsorted lists. Check each element one by one."""
#EX: nums = [10,20,30,40]     Search 30 → found at index 2
#We check each element one by one until we find the target.
"""nums = [10, 20, 30, 40, 50]
target = int(input("Enter element to search: "))
found = -1
for i in range(len(nums)):
    if nums[i] == target:
        # If the element is found, update the 'found' variable to the current index 'i'.
        found = i
        break
if found != -1:
    # If the element was found, print a message showing the index where it was located.
    print("Element found at index:", found)
# If the condition 'found != -1' is false, this 'else' block will run.
else:
    print("Element not found")"""

#Binary Search: Works only on sorted lists. Divide list into halves repeatedly until element is found.
"""nums = [10, 20, 30, 40, 50]
target = int(input("Enter element to search: "))
# Initialize a pointer 'low' to the first index of the list (0).
low = 0
# Initialize a pointer 'high' to the last index of the list (len(nums)-1, which is 4 here).
high = len(nums) - 1 #4
found = -1
while low <= high:
    mid = (low + high) // 2  #calculates the middle index: mid = (0 + 4) // 2 = 2.
    #It checks the element at nums[2], which is 30.
    # Check if the element at the middle index is our target.
    if nums[mid] == target:  #The condition nums[mid] == target (30 == 40) is false.
    # If it is, we've found it! Store the index in the 'found' variable.
        found = mid
        # Exit the loop immediately since there's no need to search further.
        break
    # If the middle element is LESS THAN the target...
    elif nums[mid] < target:   #The condition nums[mid] < target (30 < 40) is true. 
        #The low pointer is updated to mid + 1. So, low becomes 2 + 1 = 3.
         low = mid + 1
    
else:
        high = mid - 1
# After the loop finishes, check if the 'found' variable was ever updated.
if found != -1:
    # If 'found' is not -1, the element was found. Print its index.
    print("Element found at index:", found)
else:
    # If 'found' is still -1, the loop completed without finding the element.
    print("Element not found")"""


#print vowels from a list of characters
"""cities = ["hyderabad", "mumbai", "Banglore", "Kolkata", "chennai"]
vowels = "aeiouAEIOU"   # include uppercase vowels also
for city in cities:               # loop through each city
    print("City:", city)
    for ch in city:               # check each character in the city name
        if ch in vowels:          # if character is a vowel
            print(ch, end=" ")    # print vowel
    print()  # move to next line after each city"""

"#Two sum problem"
"""You are given an array of integers nums and an integer target.
Write a Python program to find two numbers in the array 
such that they add up to the given target."""

# Example Input
nums = [2, 7, 11, 15]          # A list (array) of integers.
target = 26
# Solution using loops
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):   # Inner loop: j starts from the next index after i (i+1)
                                        # to avoid using the same element twice and to avoid duplicate pairs.
                                        # For i=0 → j: 1,2,3 ; for i=1 → j: 2,3 ; etc.
        # Check if the numbers at positions i and j add up to the target.
        if nums[i] + nums[j] == target: # Compare the sum of the two chosen elements with target.
            print([i, j])