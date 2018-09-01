
# ======================
# nestedforloops.py
# ======================

# Using "nested for loops",  "list comprehension inside a for loop" and "Nested comprehension"

# We will use them here to display lists of all all the locations that lead to the destinations.

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

# ========================
# using nested for loops
# ========================

print("nested for loops:")
print("-----------------")

for loc in sorted(locations):
    exits_to_destination_1 = []
    for xit in exits:
        if loc in exits[xit].values():
            exits_to_destination_1.append((xit, locations[xit]))
    print("Locations leading to {}".format(loc), end='\t')
    print(exits_to_destination_1)

print("="*20)


# Results:

# nested for loops:
# -----------------
# Locations leading to 0	[(0, 'Beginning'), (1, 'Road'), (2, 'Hill'), (3, 'Building'), (4, 'Valley'), (5, 'Forest')]
# Locations leading to 1	[(3, 'Building'), (4, 'Valley'), (5, 'Forest')]
# Locations leading to 2	[(1, 'Road'), (4, 'Valley'), (5, 'Forest')]
# Locations leading to 3	[(1, 'Road')]
# Locations leading to 4	[(1, 'Road')]
# Locations leading to 5	[(1, 'Road'), (2, 'Hill')]


# =============================================
# using list comprehension inside a for loops:
# =============================================

print("Using List comprehension inside a for loop:")
print("-------------------------------------")

for loc in sorted(locations):
    exits_to_destination_2 = [(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
    print("Locations leading to {}".format(loc), end='\t')
    print(exits_to_destination_2)
print("="*20)

# Results:

# Using List comprehension inside a for loop:
# -------------------------------------
# Locations leading to 0	[(0, 'Beginning'), (1, 'Road'), (2, 'Hill'), (3, 'Building'), (4, 'Valley'), (5, 'Forest')]
# Locations leading to 1	[(3, 'Building'), (4, 'Valley'), (5, 'Forest')]
# Locations leading to 2	[(1, 'Road'), (4, 'Valley'), (5, 'Forest')]
# Locations leading to 3	[(1, 'Road')]
# Locations leading to 4	[(1, 'Road')]
# Locations leading to 5	[(1, 'Road'), (2, 'Hill')]


# =============================
# using Nested comprehensions:
# =============================
# This one produces a list with all the above exits to each location.
# We will format it in next section.


print("Using Nested Comprehensions:")
print("----------------------------")

exits_to_destination_3 = [[(xit, locations[xit]) for xit in exits if loc in exits[xit].values()] for loc in sorted(locations)]
print(exits_to_destination_3)
print("="*20)

# Results:
# all in one line

# Using Nested Comprehensions:
# ----------------------------
# [[(0, 'Beginning'), (1, 'Road'), (2, 'Hill'), (3, 'Building'), (4, 'Valley'), (5, 'Forest')], [(3, 'Building'),
# (4, 'Valley'), (5, 'Forest')], [(1, 'Road'), (4, 'Valley'), (5, 'Forest')], [(1, 'Road')], [(1, 'Road')], [(1, 'Road'), (2, 'Hill')]]


# ==================================================
# Nested comprehensions using "enumerate" function:
# ==================================================

# We can use the enumerate function to get the index of each list in the other list

print("format using enumerate:")
print("------------------------")
for index, loc in enumerate(exits_to_destination_3):  # unpacking exits_to_destination_3 into index and loc
    print("Locations leading to {}".format(index), end='\t')
    print(loc)
print("="*20)


# Results

# format using enumerate:
# Locations leading to 0	[(0, 'Beginning'), (1, 'Road'), (2, 'Hill'), (3, 'Building'), (4, 'Valley'), (5, 'Forest')]
# Locations leading to 1	[(3, 'Building'), (4, 'Valley'), (5, 'Forest')]
# Locations leading to 2	[(1, 'Road'), (4, 'Valley'), (5, 'Forest')]
# Locations leading to 3	[(1, 'Road')]
# Locations leading to 4	[(1, 'Road')]
# Locations leading to 5	[(1, 'Road'), (2, 'Hill')]

# =============================
# Python built in functions:
# =============================
# Python has many built-in functions like enumerate
# Its good to be familiar with all built-in functions because they can save you lots of time

# Check built-in functions here
# https://docs.python.org/3/library/functions.html





