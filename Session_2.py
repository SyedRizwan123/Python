
#Bitwise Operators
"""a=10  
b=6
print(a & b)""" #2

"""a=10  
b=6
print(a | b)"""

"""a=10
b=6
print(a^b)"""




#Membership Operators
"""my_List = [1, 2, 3, 4, 5]
a=3
b=7
print(a in my_List)  #True
print(b in my_List)  #False
print(a not in my_List)  #False
print(b not in my_List)  #True"""

#a=10
"""print(a<<1)
print(a<<2)
print(a<<3)"""

"""print(10>>1)
print(10>>2)"""

#Bodmas
"""BODMAS Rule

The BODMAS rule is a sequence that tells us the correct order of operations when solving mathematical expressions.

BODMAS stands for:

B → Brackets (solve inside brackets first)

O → Orders (powers, roots, exponents, square roots, etc.)

D → Division (÷)

M → Multiplication (×)

A → Addition (+)

S → Subtraction (−)"""

"""result = 10+(3*-8)/4      #-24/4=-6+10=4
print(result)

result1=4**2+5/2*3     #16,   2.5 7
print(result1)"""

#Addition of two numbers
"""a=int(input("Enter a number"))
b=int(input("Enter a second number"))
sum=a+b
print(sum)"""

"""a=10
b=20
a,b=b,a
print(a)
print(b)"""


"""Statement = True
if Statement:
    print("Hello Python")"""

#if...else
"""x=10
y=20
if x>y:
    a=x+y
    print(a)
else:
    b=y-x
    print(b)  #10"""

#leap year
"""year=int(input("Enter a year: "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")"""

#Nested if...else
"""num=int(input("Enter a number: ")) #5
if num>=0:
    if num==0:
        print(num,"is zero")
    else:
        print(num,"is a positive number")
else:
    print(num,"is a negative number")"""


#for loop
"""for i in range(5):
    print(i,"Hello Python")"""

"""for number in range(0,11):
   print(number)"""

"""for number in range(0,10,3):
    print(number)"""

"""for number in range(5,-1,-1):
    print(number)"""

#looping list
"""my_list=[1,2,3,4, "python","is","neat"]
for item in my_list:
    print(item)"""

#Break statement
"""my_list=[1,2,3,4, "python","is","neat"]
for item in my_list:
    if item=="python":
        break
    print(item)"""

#continue
"""my_list=[1,2,3,4, "python","is","neat"]
for item in my_list:
    if item=="python":
        continue
    print(item)"""

#while loop
"""number = 1
while number <= 3:
 print(number)
 number = number + 1"""

#Palidrome : A palindrome is a word, phrase, number, or sequence of characters that reads the same forward and backward ex:121
"""num = int(input("Enter your number"))  #121        #num=12       #num=1  num=0
temp = num
rev = 0
#rem
while num != 0:
    rem = num % 10         #rem=121%10=1 rem=1     rem=12%10=2       rem=1%10=1
    rev = rev * 10 + rem   #rev=0*10+1=1           rev=1*10+2=12     rev=12*10+1=121
    num = num // 10         #num=121/10=12         num=12//10=1       num//10=0

print(f"rev value = {rev}")    #121

if temp == rev:      #121==121
    print("Given number is palindrome")
else:
    print("Given number is not palindrome")"""

#program to find the length of a number
"""num = int(input("Enter any value: "))  #1234
count = 0
while num != 0:         #1234 !=0
    num = num // 10     #1234//10=123
    count += 1          #count=1, count=2, count=3, count=4
print(f"The number of digits is: {count}")"""

#nested loop
"""for i in range(1, 4):        # Outer loop → rows
    for j in range(1, 4):       # Inner loop → columns
        print(i * j, end="  ")
    print()"""  # new line after inner loop


#Armstrong Number
#153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084, 548834, 1741725
num = int(input("Enter any value: "))
temp = num
Arm = 0
count = 0

# Count number of digits
n = num
while n != 0:
    count += 1  # Increment count for each digit found in the number 
    n //= 10

# Compute sum of digits raised to count (power)
n = num   # Reset n to original number
while n != 0:
    rem = n % 10
    Arm= Arm + rem ** count   # use count as exponent
    n //= 10

print(f"The sum of digits^{count} = {Arm}")

if temp == Arm:
    print("Given number is an Armstrong number")
else:
    print("Given number is not an Armstrong number")
