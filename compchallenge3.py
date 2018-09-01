
# ====================
# compchallenge3.py
# ====================

# Convert all comprehensions in the previous challenge to "for loops"
# We started off by creating a list comprehension from a "for loop",
# This challenge is to go the other way.
# Convert each of the comprehensions in the previous challenge into a "for loop" that produces the same result


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

# =========
# Part 1:
# =========

# ==================================
# Original code with comprehension
# ==================================

loc = 1
forest = [locations[xit] for xit in exits if loc in exits[xit].values()]
print(forest)
print("="*20)

# Results:

# ['Building', 'Valley', 'Forest']

# ======================================================
# New code using "for loop" should produce same results
# ======================================================

loc = 1
forest = []
for xit in exits:
    if loc in exits[xit].values():
        forest.append(locations[xit])
print(forest)
print("="*20)

# Results:

# ['Building', 'Valley', 'Forest']


# =================================================================================

# =========
# Part 2:
# =========

# ==============================================
# This is the original code using comprehension
# ==============================================

for loc in sorted(locations):  # iterates through all locations and sorts them.
    forest = [(exit, locations[exit]) for exit in exits if loc in exits[exit].values()]
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

# =======================================================
# New code using "for loop" should produce same results
# =======================================================

for loc in sorted(locations):
    forest = []  # initialize to empty list
    for xit in exits:
        if loc in exits[xit].values():
            forest.append((xit, locations[xit]))  # use double quotation because it will produce tuple with number (xit) and location name
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

