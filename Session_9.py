"""numbers = [12, 45, 67, 2, 89, 34]
print("Largest:", max(numbers))
print("Smallest:", min(numbers))"""

#Reverse a list without using built-in reverse()
"""numbers = [1, 2, 3, 4, 5]
reversed_list = numbers[::-1]
print("Reversed:", reversed_list)"""

#Check if a list is a palindrome
"""list1 = [1, 2, 3, 2, 1]
if list1 == list1[::-1]:
    print("Palindrome List")
else:
    print("Not Palindrome")"""

#Tuples():Tuples are immutable sequance, typically used to store collections of heterogenious (mixed_list = [1, "two", 3.0, True]  # A list with elements of different data types is heterogeneous.
#data, or for cases where an immutable sequnce of homogeniuos data is needed
#declaring empty tuple
#tuple1= ()
#print(type(tuple1))
#print("tuple1:", tuple1,len(tuple1))

#single element tuple must have a traling comma
#tuple3=(1,)      #tuple3=(1) will throw a syntax error
#print("tuple3:", tuple3, len(tuple3))

#tuple operations:Limited since unlike list, tuple are immutable
#tuple4=(1,2,3)
#print("tuple4:", tuple4, len(tuple4))

#you can index tuple just like lists
#tuple4=(1,2,3)
#print("tuple4:", tuple4[0],tuple4[1],tuple4[2])

#You can slice tuples just like lists
#tuple4=(1,2,3)
#print("tuple4:", tuple4[0:2], tuple4[0:3])

#You can also nest tuples like lists
#tuple5=(1,2,3),(4,5,6)
#print("tuple5[1][2]:", tuple5[1][2])

#tuple5=(1,2,3)+(4,5,6)
#print("tuple5:", tuple5, len(tuple5))

#converted into List
"""my_tuple=(1,2,3,4,5)
print(my_tuple)
print(type(my_tuple))
my_list=list(my_tuple)
print(my_list)
print(type(my_list))"""

#a,b,c=10,7,8
#print(c,b,a)

#tuple packing and unpacking
#multiple assignment is essentially packing/unpackung in action

#tuple packing
"""tuple7= 1,2,3   #(1,2,3)
print("tuple7:", tuple7, len(tuple7))

#tuple unpacking
x,y,z=tuple7
print("tuple unpacking:", x,y,z)"""


#we can convert list in tuples
"""tuple6=tuple([1,2,3])
print(type(tuple6))
print("tuple6:", tuple6, len(tuple6))"""


#Repeating Elements: Given colors = ("red", "blue"),repeat it 3 times using *.
"""colors = ("red ", " blue")
# Repeat the tuple 3 times using the * operator.
# The result is a new tuple with the original elements repeated in sequence.
repeated_colors = colors * 3
repeated_element = colors[0] * 3
print(repeated_colors)
print(repeated_element)"""

#Check Membership
"""animals = ("dog", "cat", "lion", "tiger")
# Check if "cat" exists in the tuple and store the boolean result in the variable 'is_cat_present'
is_cat_present = "cat" in animals

# Check if "elephant" exists in the tuple and store the boolean result in the variable 'is_elephant_present'
is_elephant_present = "elephant" in animals
# Print the result for "cat"
print(f"Is 'cat' present in the tuple? {is_cat_present}")
# Print the result for "elephant"
print(f"Is 'elephant' present in the tuple? {is_elephant_present}")"""

#Tuple of Tuples Given students = (("Alice", 20), ("Bob", 22), ("Charlie", 19)), print all student names and ages.
#output: Alice is 20 years old, Bob is 22 years old, Charlie is 19 years old.

"""students = (("Alice", 20), ("Bob", 22), ("Charlie", 19))
for student in students:
    name, age = student
    print(f"{name} is {age} years old")"""

#set:set is a data structure A set is a collection of unique items, with the structural implementation of the set not allowing duplicate values a set is defined by curly braces{}

"""set1={1,2,3}
print(type(set1))
print(set1)
print(len(set1))"""

"""tuple=(1,1,2,3)
print(tuple)"""

#Add an element
"""we can add an element to an existing set by using the add function . The resulting set will ensure uniquness of the added value within the set. 
An add operation modifies the original set """
"""set1={1,2,3}
set1.add(4)
set1.add(2)
print(set1)"""

#Find element:
"""We can search a set to see if a specified element is present within the set.
This can be done using the in 'keyword'""" 
"""set1={1,2,3}
contains2 = 2 in set1
contains4 = 4 in set1
print("Contains 2:", contains2)
print("Contains 4:", contains4)"""

#Remove an element
"""We can remove an element from a set by using the remove function.
A remove operation modifies the original set""" 
"""set1={1,2,3}
set1.remove(2)
#print(set1)

set1.add(2)
print(set1)"""

#We cannot attempt to remove an inexistent element from the set. The operation will
#return in 'keyerror' if the specified element to be removed is not found within the set"""
"""set1 = {1,2,3}
set1.remove(4)
print(set1)"""


"""To prevent an accidental 'KeyError', we can always check to see if the element is present within the 
set or not before attempting a delete operation"""
#if condition
"""set1={1,2,3}
if 4 in set1:
    set1.remove(4)
print(set1)"""

#pop element
"""We can pop out a randomm element from the set. This is usually done when to iterate over
the set to fully consume it. What we mean by consume is, we don't want the value we popped to be present within the set;
and we will continue to do so unit the set is empty"""
"""my_set = {1,2,0,3,4,5}
popped_element = my_set.pop()
print(popped_element)
print(my_set)"""

"""set1 = {1,2,3}
for a in range(len(set1)):
    print('pop:', set1.pop())
print('set1:', set1)"""

#union
#We can create a union of 2 sets, which creates a new set containing unique elements found across both the sets
"""set1={1,2,3}
set2={2,3,4}
set3=set1.union(set2)
print("union:", set3)"""

#A union can also be performed using pipe operator
"""set1 = {1,2,3}
set2 = {2,3,4}
set3=set1 | set2
print(set3)"""

#intersection
"""One can performm an intersection operation on sets. This results in a set that contains elements
which are present in both sets. Let us take the same example as before, but this time we will do an intersection operation"""
set1={1,2,3}
set2={2,3,4}
set3= set1.intersection(set2)
print(set3)

#intersection can also be performed by using '&' operator
set1 = {1,2,3}
set2 = {2,3,4}
set3=set1 & set2
print(set3)
