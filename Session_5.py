#Find the ASCII value of a given character
"""ch = input("Enter a character: ")   #a-97 to z-122,  A-65 to Z-90
ascii_value = ord(ch)    #ord() function is used to find the ASCII value of the character.
print("The ASCII value of", ch, "is", ascii_value)"""

#Calculator App
"""num1=int(input("Enter your number"))
sign=input("enter your sign")
num2=int(input("enter a number"))
if sign=="+":
    print(num1+num2)
elif sign=="-":
    print(num1-num2)
elif sign=="*":
    print(num1*num2)
elif sign=="/":
    print(num1/num2)
else:
    print("invalid sign")"""

#To find given number is Strong number or not
#Strong number:A Strong number is a number where the sum of the factorials of its digits equals the number itself.
# //ex:145: find factorial with each digit 1!+4!+5!=145 we have to get same digit
"""num = int(input("Enter a number: "))
sum = 0    # sum is used to store the sum of the factorials of the digits.
temp = num #temp stores the original number for comparison later.
while num:
    i = 1
    fact = 1
    r = num % 10 # Extract the last digit 

    while i <= r:    # Calculate factorial of the digit       #1<=5
        fact = fact * i        #fact=1*1=1 fact=1*2=2, fact=2*3=6 fact=6*4=24, fact=24*5=120
        i += 1
    sum = sum + fact  # Add factorial to sum     #sum=0+120=120 //120+24=144  sum=144  sum=144+1=145
    num = num // 10   # Remove the last digit    #num=145/10=14 //14/10=1 num=1       num=144+1=145
if sum == temp:
    print(f"{temp} is a Strong number")
else:
    print(f"{temp} is not a Strong number")"""

# perfect number: A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding itself).
# 6=1+2+3 =6 6 devisors is 1+2+3
"""num = int(input("Enter a number: "))
sum = 0
for i in range(1, num):  # num=5   1<5
    if num % i == 0:  # 6%1==0   6%1==0   6%2==0  6%3==0  6%4=
        sum += i  # sum=0+1=1     sum=1+2=3   sum=3+3=6                      3+4=7
if sum == num:
    print(f"{num} is a Perfect number")
else:
    print(f"{num} is not a Perfect number")"""

#print only even number
"""for i in range(0, 11, 1):    #0+2=2, 2+2=4,
    if i % 2 == 0:
        print(i, "= even")
    else:
        print(i, "= odd")
"""
# print only odd number
"""for i in range(1, 11, 2):
    if i % 2 == 0:
        print(i, "= even")
    else:
        print(i, "= odd")"""

#print 2nd table
"""n = int(input("Enter a number: "))  
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")"""

#Sum of natural numbers
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum = sum + i
print("The sum of first", n, "natural numbers is:", sum)
