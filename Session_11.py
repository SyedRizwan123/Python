# Create a dictionary using dict() constructor
"""my_dict = dict(food="ham", drink="beer", sport="football")
# Print the dictionary before removing anything
print(f"dict before pops: {my_dict}")
food = my_dict.pop("drink")
print(f"popped value {food}")
print(f"dict after pop {my_dict}")

# pop("food", "default value for food")
# → removes "food" key and returns its value ("ham")
# If "food" was NOT in the dictionary, it would return the default value instead
food_again = my_dict.pop("food", "default value for food")
print(f"food again: {food_again}")"""  
# Output: food again: ham

#dict.setdefault: its a one of the command
#Return the value of key defined as first parameter. if the key is not present in the dict, adds key with default value (second parameter)
"""my_dict={"a":1,"b":2,"c":3}
print(my_dict)
a=my_dict.setdefault("a","my default value")
d=my_dict.setdefault("d","my default value")

print(a)
print(d)
print(my_dict)"""

#dict.update: Merge two dicts
"""dict1={"a":1, "b":2,}
dict2={"c":3}
dict1.update(dict2)
print(dict1)

#if they have same keys
dict1.update({"c":4})
print(dict1)"""

#we can also give list values to key
#good_dict={"mykey": ["python", "is","still", "cool"]}
#print(good_dict)

#Count Word Occurrences in a Sentence using Dictionary"
# Define a string (sentence) in which we want to count word occurrences
"""sentence = "python is easy and python is powerful"
# Create an empty dictionary to store words as keys and their counts as values
word_count = {}
# Loop through each word in the sentence after splitting it by spaces
for word in sentence.split():
    # sentence.split() → splits the sentence into ['python', 'is', 'easy', 'and', 'python', 'is', 'powerful']
    # For each word, get its current count from the dictionary
    # If the word is not found, default value 0 is returned
    # Then we add 1 to the count
    word_count[word] = word_count.get(word, 0) + 1  # word_count.get(word, 0) fetches the current count of 'word' from 'word_count'.
Step 1: Understanding word_count.get(word, 0)
.get(key, default_value) is a dictionary method
It tries to get the value for the given key (word)
If the key exists, it returns its current value
If the key doesn't exist, it returns the default_value (0 in this case)

Step 2: The Complete Process
Get current count: word_count.get(word, 0)
Add 1: + 1
Store back: word_count[word] = ...
Let's Trace Through the Example
Sentence: "python is easy and python is powerful"
Words: ['python', 'is', 'easy', 'and', 'python', 'is', 'powerful']

Iteration 1: word = "python"
word_count.get("python", 0) → "python" not in dictionary → returns 0

0 + 1 → 1

word_count["python"] = 1

Dictionary becomes: {"python": 1}

Iteration 2: word = "is"
word_count.get("is", 0) → "is" not in dictionary → returns 0
0 + 1 → 1
word_count["is"] = 1
Dictionary becomes: {"python": 1, "is": 1}

Iteration 3: word = "easy"
word_count.get("easy", 0) → "easy" not in dictionary → returns 0

0 + 1 → 1
word_count["easy"] = 1
Dictionary becomes: {"python": 1, "is": 1, "easy": 1}

Iteration 4: word = "and"
word_count.get("and", 0) → "and" not in dictionary → returns 0

0 + 1 → 1
word_count["and"] = 1
Dictionary becomes: {"python": 1, "is": 1, "easy": 1, "and": 1}

Iteration 5: word = "python" (second occurrence)
word_count.get("python", 0) → "python" exists with value 1 → returns 1

1 + 1 → 2
word_count["python"] = 2
Dictionary becomes: {"python": 2, "is": 1, "easy": 1, "and": 1}

Iteration 6: word = "is" (second occurrence)
word_count.get("is", 0) → "is" exists with value 1 → returns 1

1 + 1 → 2
word_count["is"] = 2
Dictionary becomes: {"python": 2, "is": 2, "easy": 1, "and": 1}

Iteration 7: word = "powerful"
word_count.get("powerful", 0) → "powerful" not in dictionary → returns 0

0 + 1 → 1
word_count["powerful"] = 1
Final dictionary: {"python": 2, "is": 2, "easy": 1, "and": 1, "powerful": 1}"""

# Finally, print the dictionary containing each word and its occurrence count
#print("Word Count:", word_count)
#Output: {'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1}
 

# Merging Two Dictionaries
# Create the first dictionary with two key-value pairs
"""dict1 = {"a": 1, "b": 2}
# Create the second dictionary with two key-value pairs
dict2 = {"c": 3, "d": 4}
# Merge both dictionaries using dictionary unpacking (**)
# {**dict1, **dict2} → expands the key-value pairs from both dictionaries
# and creates a new dictionary that contains all of them.
# If both have the same key, dict2’s value will overwrite dict1’s.
merged = {**dict1, **dict2}
print("Merged Dictionary:", merged)"""

#Check if a key exists in dictionary
"""student = {"name": "Rahul", "age": 21, "course": "Python"}
# Take input from the user
key = input("Enter your key: ")
# Check if the entered key exists in the dictionary
if key in student:
    print("Key exists")
else:
    print("Key does not exist")"""

# Create a dictionary of numbers and their squares using a loop
"""n = 5  
squares = {} 
for i in range(1, n+1):
    squares[i] = i * i
print("Squares Dictionary:", squares)"""