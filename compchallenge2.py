
# =====================
# compchallenge2.py:
# =====================

# ========
# Part 1:
# ========
# Create a comprehension that returns a list of all the locations that have an exit to the forest.
# The list should contain the description of each location, if it's possible to get to the forest from there.
#
# The forest is location 5 in the locations dictionary
# The exits for each location are represented by the exits dictionary.
#
# Remember that a dictionary has a .values() method, to return a list of the values.
#
# The forest can be reached from the road, and the hill; so those should be the descriptions that appear in your list.
#
# Test your program with different destinations (such as 1 for the road) to make sure it works.
#
# ========
# Part 2:
# ========
# Once it's working, modify the program so that the comprehension returns a list of tuples.
# Each tuple consists of the location number and the description.
#
# Finally, wrap your comprehension in a for loop, and print the lists of all the locations that lead to each of the
# other locations in turn.
# In other words, use a for loop to run the comprehension for each of the keys in the locations dictionary.
 
 
locations = {0: "Beginning",
             1: "Road",
             2: "Hill",
             3: "Building",
             4: "Valley",
             5: "Forest"}
 
exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}


# ==================
# Part 1 solution:
# ==================

# This comprehension gives a list of locations that have exit to the forest (5)
# This means that their exits contain a 5
# Explanation:

# Conditional comprehension have three sections: Expression, iteration and filter(s)
# <<= Expression <<==> Iteration <<==>>Filter(s)

# In this case, Expression is ==> locations[exit]
# This pulls the locations name, with the exit chosen

# Iteration is ==> for exit in exits
# This loops through all exits above. from 0 trough 5

# Filter is ==> if loc in exits[exit].values()
# exits[exit] indicates say exits[0], then .values() pulls the numbers in the dictionary

# So if numbers in the dictionary match 5, then it prints the name of that exit ==> locations[exit]
# See more explanation in below test code.

loc = 5  # this is the exit we are looking for
forest = [locations[exit] for exit in exits if loc in exits[exit].values()]
print(forest)

# Results:
# ['Road', 'Hill']


# =========================================
# My test code to help me understand above:
# =========================================

for exit in exits:  # loops through exists
    print("exit = {}".format(exit))     # returns exits 0 through 5
print("="*20)

# results:

# exit = 0
# exit = 1
# exit = 2
# exit = 3
# exit = 4
# exit = 5

# =============================
# Loops through exits and prints dictionary values of each exit.

for exit in exits:  # Loops through exists
    print(exits[exit].values())  # Prints dictionary values of each exit
print("="*20)

# Results:

# dict_values([0])
# dict_values([2, 3, 5, 4, 0])
# dict_values([5, 0])
# dict_values([1, 0])
# dict_values([1, 2, 0])
# dict_values([2, 1, 0])

# =================================
# Prints the dictionary value in exits if any of its value matches 5 (loc)

print("loc = {}".format(loc))
for exit in exits:  # Loops through exists
    if loc in exits[exit].values():  # if loc (5) is in the exits values
        print(exits[exit].values())  # Print dictionary values of each exit that has a 5 in it
        print(locations[exit])       # print the location with 5, in this case, it is Road and Hill
        print("="*10)

# Results:

# loc = 5
# dict_values([2, 3, 5, 4, 0])
# Road
# ==========
# dict_values([5, 0])
# Hill


# ================================================================================

# ===================
# Part 2 solution:
# ===================

# Once it's working, modify the program so that the comprehension returns a list of tuples.
# Each tuple consists of the location number and the description.

# Here we just need to include exit keys since we already have the names.
# We add (exit, locations[exit]) instead of original locations[exit]


loc = 5
forest = [(exit, locations[exit]) for exit in exits if loc in exits[exit].values()]
print(forest)
print("="*20)

# Results:

# [(1, 'Road'), (2, 'Hill')]

# ====================================================================
# Scope of values in comprehensions is confined to the comprehension
# ====================================================================

# In below code, if you hover around "exit" in LINE_1, it says "Shadows built-in name 'exit'
# We would want to rename exit into something else, say Xit
# if we refactor, you will see it only changes exit in LINE_1 and not LINE_2
# So although LINE_1 and LINE_2 uses same name "exit", it refers to different variables in each case.
# So the scope of the exit is confined to the comprehension.


forest = [locations[Xit] for Xit in exits if loc in exits[Xit].values()]  # LINE_1: "Xit" was initially "exit"
print(forest)
print("*"*10)

forest = [(exit, locations[exit]) for exit in exits if loc in exits[exit].values()]  # LINE_2:
print(forest)
print("="*20)


# ===========================================
# Using for loops in nexted comprehensions:
# ===========================================

# This will demonstrate that we can use for loop in a nested comprehension
# We will check for locations leading to all exits using this code


for loc in sorted(locations):  # iterates through all locations and sorts them.
    forest = [(exit, locations[exit]) for exit in exits if loc in exits[exit].values()]  # LINE_2:
    print("Locations leading to {}".format(loc), end='\t')
    print(forest)
print("="*20)

# Results:

# Locations leading to 0	[(0, 'Beginning'), (1, 'Road'), (2, 'Hill'), (3, 'Building'), (4, 'Valley'), (5, 'Forest')]
# Locations leading to 1	[(3, 'Building'), (4, 'Valley'), (5, 'Forest')]
# Locations leading to 2	[(1, 'Road'), (4, 'Valley'), (5, 'Forest')]
# Locations leading to 3	[(1, 'Road')]
# Locations leading to 4	[(1, 'Road')]
# Locations leading to 5	[(1, 'Road'), (2, 'Hill')]









