#Program to check if two strings are anagrams
"""An anagram is a word or phrase formed by rearranging the letters of another word  using all the original letters exactly once. 
For example, listen" and "silent" are anagrams because both use the same letters in a different order."""
"""str1 = "listen"
str2 = "client"
# Sort both strings and compare
print(sorted(str1))  #['e', 'i', 'l', 'n', 's', 't']
print(sorted(str2))  #['e', 'i', 'l', 'n', 's', 't'
if sorted(str1) == sorted(str2):
    print("Anagrams")
else:
    print("Not anagrams")"""

# Program to remove all duplicate characters from a string
"""input_string = "programming"
result_string = ""
for char in input_string:
     if char not in result_string:
          result_string += char
print("Original string:", input_string)
print("String after removing duplicates:", result_string)"""

#List: List are mutable sequance, typically used to store collections of homogenious items
listpeople = ["tom","harry","jane","liz"]
"""print(type(listpeople))
print(listpeople)"""
listflowers = ["rose","lily","tulip","jasmine"]
listpets = ["cat","turtle","goat","dog"]
listnumfriends = [21,33,10,51]

#List of heterogenious items are not incorrect, just atypical
#listAtypical = [1,'cat',0x43,567.55]       #0x45 UTF-8 ENCODING FOR 69
#print(listAtypical)

#concatenate lists
#listCon= listpeople + listflowers
#print("listcon->", listCon)

#Length of lists
#print("length position->",len(listpeople))

#refer to item in list with index
#print("listpeople[2]->", listpeople[2])
#print("listpeople[-3]->", listpeople[-3])

#slice list with [startindex:endindex]
#print("listpeople[2:]->", listpeople[1:4])

#unlike strings, Lists are mutable
#assign to an index, we can update a value
#print(listpets)
#listpets[0]='t-rex'
#listpets[2]='Puppy'
#print(listpets)

#Assign to a slice
listpets[0:2] =['python','elephant']
print(listpets)

#delete with slice
#listpets[2:4]=[]
#print(listpets)

#append new items to list
#listpets.append('fox')
#print(listpets)

#nested list
"""nestedlist=[listpeople,listflowers]
print(nestedlist)

print("listpeople --> ", nestedlist[0])
print("listflowers --> ", nestedlist[1])

print(nestedlist[0][1])
print(nestedlist[1][0])"""

#lists with integers
list1=[100,200,300]
list2=[5,15,25]
list3=[10,50,50,20,0,10,50]
print(list1)
print(list2)
print(list3)
list1.append(-400)   #Add an item to the end of the list. equalent to list
print("list1 Append:",list1)

list2.extend(list1)  #Extend the list2 by appending all the itimes    in list1.
print("list2extend:", list2)

list2.remove(-400)  #Remove the first item from list2 whose value is -400.
print("list2 Remove Element:",list2)

del list2[3]       #Remove the item at index[6]
print("delete list2[3]:", list2)  #[5, 15, 25, -400, 100, 200]

list2.pop()       #Remove and returns the last item in the list
print("list2 pop():", list2)

print("Index of an element:", list3.index(50)) #Returns the index in list3 of element position
print(list3.count(50))   #print the number of times 50 appears in list

list3.reverse()    #Reverse the items of list3 in place
print("list3 Reverse:", list3)

list3.sort()      #Sort the items of list3 in place
print("list3 sorted:",list3)

list3.clear()      #Remove all items from the list
print("list3 clear:",list3)

del list3        #Delete the list
#print("delete list3:", list3)
#print(list3)

for items in list1:
    print(items)