#Pattern programs
"""for r in range(4):       #rows
    for c in range (6):  #columns
        print("*", end="")
    print()  #to move next line"""

"""for i in range(1, 7):
    for j in range(1, 7):
        if j <= i:
            print("*", end="")
        else:
            print(" ", end="")
    print()"""

"""n = 5
for i in range(1, n+1):
    print("* " * i)"""

#Inverted Right Triangle
"""n = 5   # Step 1: Assign the value 5 to variable 'n'. 
        # This means the pattern will have 5 rows.
# Step 2: Loop starts from 'n' down to 1, with step -1 (decreasing order).
for i in range(n, 0, -1):
    # Step 3: For each row, print '* ' repeated 'i' times.
    print("* " * i)
    # Example:
    # When i=5 → "* " * 5 = "* * * * * "
    # When i=4 → "* " * 4 = "* * * * "
    # When i=3 → "* " * 3 = "* * * "
    # When i=2 → "* " * 2 = "* * "
    # When i=1 → "* " * 1 = "* " """

#Left Triangle of Stars
"""n = 5   # Step 1: Assign 5 to variable 'n'. 
        # This means the triangle will have 5 rows.
# Step 2: Loop from 1 to n (inclusive).
for i in range(1,n+1):    
    # When n=5 → i takes values: 1, 2, 3, 4, 5
    
    # Step 3: "  " * (n-i) → adds spaces before stars to shift them to the right
    # Step 4: "* " * i → prints stars, count increases with each row
    print("  " * (n-i) + "* " * i) 
    # Example:
    # i=1 → "  " * (5-1) + "* " * 1 = "        " + "* " = "        * "
    # i=2 → "  " * (5-2) + "* " * 2 = "      " + "* * " = "      * * "
    # i=3 → "  " * (5-3) + "* " * 3 = "    " + "* * * " = "    * * * "
    # i=4 → "  " * (5-4) + "* " * 4 = "  " + "* * * * " = "  * * * * "
    # i=5 → "  " * (5-5) + "* " * 5 = "" + "* * * * * " = "* * * * * """

#inverted
"""n = 5   # Step 1: Assign 5 to variable 'n'. 
        # This means the triangle will have 5 rows.

# Step 2: Loop from 1 to n (inclusive).
for i in range(n,0, -1):    
    print("  " * (n-i) + "* " * i) 
    # Example:
    # i=1 → "  " * (5-1) + "* " * 1 = "        " + "* " = "        * "
    # i=2 → "  " * (5-2) + "* " * 2 = "      " + "* * " = "      * * "
    # i=3 → "  " * (5-3) + "* " * 3 = "    " + "* * * " = "    * * * "
    # i=4 → "  " * (5-4) + "* " * 4 = "  " + "* * * * " = "  * * * * "
    # i=5 → "  " * (5-5) + "* " * 5 = "" + "* * * * * " = "* * * * * """


# Simple Triangle Pattern
"""rows = 6  # Sets the total number of rows for the triangle pattern.
for i in range(1, rows):  # Loop from 1 to rows-1 (i = 1 to 5)
    spaces = rows - i - 1         # Calculate number of spaces before the stars for current row
    stars = 2 * i - 1             # Calculate number of stars for current row (odd numbers: 1, 3, 5, ...)
    print(" " * spaces + "*" * stars)  # Print spaces followed by stars on the same line
    # " " * spaces: adds leading spaces to center the triangle
    # "*" * stars: prints the required number of stars for the row"""

#inverted pyramid
"""n = 5   # Assign the number of rows for the triangle. Here, n = 5.
# Loop starts from n down to 1 with step -1.
# So, i will take values: 5, 4, 3, 2, 1
for i in range(n, 0, -1):
    # The + operator joins spaces and stars in one string for each row.
    print(" " * (n-i) + "* " * i)
    # Row-wise working:
    # i=5 → " " * 0 + "* " * 5 = "* * * * * "
    # i=4 → " " * 1 + "* " * 4 = " * * * * "
    # i=3 → " " * 2 + "* " * 3 = "  * * * "
    # i=2 → " " * 3 + "* " * 2 = "   * * "
    # i=1 → " " * 4 + "* " * 1 = "    * "  """

#Diamond Pattern
"""n = 5  # Number of rows for the upper half of the diamond
# Upper half of the diamond (including the middle row)
for i in range(1, n+1):  # Loop from 1 to n (1 to 5)
    print(" "*(n-i) + "* " * i)  
    # " "*(n-i): Prints spaces to center the stars
    # "* " * i: Prints i stars with a space after each
# Lower half of the diamond (excluding the middle row)
for i in range(n-1, 0, -1):  # Loop from n-1 down to 1 (4 to 1)
    print(" "*(n-i) + "* " * i)
    # " "*(n-i): Prints spaces to center the stars
    # "* " * i: Prints i stars with"""

#Hallow Square pattern
"""for i in range(1, 6):
    for j in range(1, 6):
        if i == 1 or j == 1 or i == 5 or j == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()"""