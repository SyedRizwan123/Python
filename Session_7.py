# This program prints a right-angled triangle pattern of numbers.
"""for i in range(1, 6):     # This is the outer loop. It will run 5 times, with 'i' taking values from 1 to 5.
                          # This loop controls the number of rows to be printed.

    for j in range(1, i + 1):  # This is the inner loop. It depends on the value of 'i' from the outer loop.
                               # For each row 'i', it will run 'i' times, with 'j' taking values from 1 up to 'i'.
                               # This loop is responsible for printing the numbers in each row.

        print(j, end=" ")    # This prints the current value of 'j' followed by a space instead of a new line.
                             # This keeps the numbers for a single row on the same line.

    print()                 # This prints a new line character after the inner loop completes.
                            # It moves the cursor to the next line, so the numbers for the next row
                            # will be printed on a new line."""


#Number Triangle Pattern Program" (also called Floyd’s Triangle in mathematics).
"""rows=4
num=1
for i in range(1,rows+1):
    for j in range (1,i+1):
        print(num, end=" ")
        num+=1
    print()"""

# This program prints a right-angled triangle pattern of letters.
"""for i in range(1, 6):       # This is the outer loop. It will iterate 5 times, with 'i' taking values from 1 to 5.
                            # This loop controls the number of rows to be printed.
    ch = 'A'    

    for j in range(1, i + 1):
        print(ch, end=' ')
        ch = chr(ord(ch) + 1)
    print()"""

"""print("Hello Python")
print("'Hello Python'")
print("\"Syed\"")
print("sayyad "*2)"""

#here i given multiple print statements then i want to print in signle line we have to use "end='..'"
"""print("we'll first learn how to print.",end=' ')
print("Then we'll learn how to comment code.")"""

#string formating:In Python, string formatting is the process of creating a formatted string by embedding variables or values within a text string. This allows you to create dynamic strings that incorporate variable values, making your code more readable and flexible.

#using '%' operator: This operator uses  to insert values into a string.
"""name = "Syed"
age = 25
#print("My name is ", name, "and  i am", age, "years old")
formatted_string = "My name is %s and I am %d years old." % (name, age)    #My name is Syed and i am 25 years old
print(formatted_string)"""

#Using 'str.format().: This method use to format strings. It allows for more flexibility in terms of the order of variables and additional formatting options.
"""name = "Syed"
age = 25
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)"""


#Using f-strings (Formatted String Literals):  f-strings are a concise and readable way to format strings. They allow you to embed expressions directly within string literals by using curly braces {}
"""name = "Zareena"
age = 22
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)"""

"""fruits="Apples and Oranges"
numapples=10
numoranges=20
print(f"I have {fruits}...I have, {numapples}Apples and ,{numoranges}Oranges")"""

#To find the Binary Value
"""decimal_number = 10
binary_value =bin(decimal_number) [2:]
print(binary_value)"""

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

#slicing and diesing
# - string can be sliced with [startIndex:endIndex]
# - startIndex is included and endIndex is excluded
# - startIndex must be < endIndex, else empty string is returned
# - if a slice index is out of range, python will go as far as it can

"""word="python"
print(word[0:3])  #prints 'pyt'
print(word[0:10]) #prints 'python'
print(word[-3:-1])  #prints 'ho'
print(word[-3:-6])  #prints ''
print(word[:2])     #prints 'py'
print(word[4:])   #prints 'on'"""

#we cant update the charecter at 0 incices 
"""word="pyhton"
word[0] = '3'
print(word)"""

print(len('python'))

print('python'.find('t')) #find index of substring in string
print('python'.startswith('p'))  # check string starts with substring
print('python'.endswith('n'))    # check string ends with substring
print('PYTHON'.lower())
print('python'.upper())
print('s'.isalpha())  #True
print('abc123'.isalnum())  #True
print('syed'.capitalize())  #Syed
print('  python  '.strip())  #python
print('python is neat'.split())   #'1','2',
print("syed rizwan".title())   #Syed Rizwan If you want each word’s first letter capitalized, use .title():
