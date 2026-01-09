#difference operation
#We can also perform a difference operation on sets. This results in a set that contains elements
# Define the two sets
"""A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}

# Calculate the difference A - B
# This operation returns a new set containing all elements that are in set A but not in set B.
difference_A_B = A - B     #output: {1, 2, 3} 
print("Difference A - B:", difference_A_B)

# Calculate the difference B - A
# This operation returns a new set containing all elements that are in set B but not in set A.
difference_B_A = B - A      #output: {6, 7}
print(difference_B_A)"""


#Symmetric Difference:
"""Symmetric difference refers to the elements that are in either of two sets, 
but not in their intersection (the elements they have in common). 
Think of it as a combination of all the unique elements from both sets"""

# Define the two sets
"""A = {10, 20, 30}
B = {30, 40, 50}
# Calculate the symmetric difference using the '^' operator.
# The symmetric difference includes elements from both sets, excluding their common elements.
# In this case, 30 is common, so it will be excluded from the result.
symmetric_difference = A ^ B
# Print the final result.
print(f"The symmetric difference is: {symmetric_difference}")
#output: The symmetric difference is: {40, 10, 50, 20}
# A set is a data structure that, by definition, does not maintain any order. This means the elements within a set have no fixed position."""

#Subset and Superset
#The subset and superset relationships between sets A and B using comparison operators.
"""A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
# Check if A is a subset of B.
# The '<=' operator returns True if all elements of A are also in B.
is_A_subset_of_B = A <= B
print(f"Is A a subset of B? {is_A_subset_of_B}")  #output: True
# Check if B is a superset of A.
# The '>=' operator returns True if B contains all elements of A.
is_B_superset_of_A = B >= A
print(f"Is B a superset of A? {is_B_superset_of_A}")"""  #output: True

#Dictionories: Collection of key-value pairs
#How to we define dictionory
#my_empty_dict={} #we have to define dictionory with {} 
#alternative: my_empty_dict=dict()  
#print(f"dict:{my_empty_dict},type:{type(my_empty_dict)}")

#initilization: How we Define
dict1={"value1":1.6, "value2":10, "name":"Syed"}
dict2= dict(value1=1.6, value2=10, name="Syed")
dict3={"value1":1.6, "value2":10, "name":"Syed", "1":"TechVertex"}  # we should not use predifine command like 'list'
"""print(dict1)
print(dict2)
print(dict3)
print(f"equals: {dict1==dict2}")  # True
print(f"lenght: {len(dict1)}")"""    # 3

#dict.keys(), dict.values(), dict.items()
"""print(f"keys: {dict1.keys()}")
print(f"values:{dict1.values()}")
print(f"items:{dict1.items()}")"""



#setting values and Accessing
#Setting the values
"""my_dict={}   #create a new dictionory
my_dict["key1"] = 10.6
my_dict["key2"] = 99
my_dict["key3"] = "Syed " """
#print(my_dict)

#Accessing values:
#print(f"value of key1: {my_dict['key1']}")

#Accessing a noneexistent key will raise "KeyError" (see dict.get(.).) for workaround):
#print(my_dict['key4'])
#Deleting a key-value pair: del dict[key]
"""my_dictn={"key1":"value1","key2":99, "keyx":"valuex"}
print("Before delete",my_dictn)
del my_dictn["keyx"]
print("Aftrer delete",my_dictn)"""

#Dictonary mutable
"""my_dict={"ham":"good", "carrot":"Semi good"}
my_other_dict=my_dict
print(my_other_dict)

my_other_dict["carrot"] = "Super tasty"   #replace in semi good
print(my_other_dict)"""
#print(my_dict)   #original dict also changed because both are pointing to same memory location

#creating new item
"""my_other_dict["sausage"]="best ever"     #cretaing a new key
print(my_other_dict)"""

#dict.get: Returns None if key is not in dict. However, you can also specify default return value which will be returned if key is not present in the dict.
"""my_dict={"a":1, "b":2, "c":3}
#value_of_d= my_dict.get("d")   #None
value_of_d = my_dict.get("d", "my default value")
print(f"value of d: {value_of_d}")"""
